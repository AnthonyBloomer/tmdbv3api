# -*- coding: utf-8 -*-

import logging
import os
import time

import requests
import requests.exceptions

from .as_obj import AsObj
from .exceptions import TMDbException

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TMDb(object):
    TMDB_API_KEY = 'TMDB_API_KEY'
    TMDB_LANGUAGE = 'TMDB_LANGUAGE'
    TMDB_WAIT_ON_RATE_LIMIT = 'TMDB_WAIT_ON_RATE_LIMIT'
    TMDB_DEBUG_ENABLED = 'TMDB_DEBUG_ENABLED'

    def __init__(self):
        self._base = 'http://api.themoviedb.org/3'
        self._remaining = 40
        self._reset = None

    @property
    def page(self):
        return os.environ['page']

    @property
    def total_results(self):
        return os.environ['total_results']

    @property
    def total_pages(self):
        return os.environ['total_pages']

    @property
    def api_key(self):
        return os.environ.get(self.TMDB_API_KEY)

    @api_key.setter
    def api_key(self, api_key):
        os.environ[self.TMDB_API_KEY] = str(api_key)

    @property
    def language(self):
        return os.environ.get(self.TMDB_LANGUAGE)

    @language.setter
    def language(self, language):
        os.environ[self.TMDB_LANGUAGE] = language

    @property
    def wait_on_rate_limit(self):
        return bool(os.environ.get(self.TMDB_WAIT_ON_RATE_LIMIT))

    @wait_on_rate_limit.setter
    def wait_on_rate_limit(self, wait_on_rate_limit):
        os.environ[self.TMDB_WAIT_ON_RATE_LIMIT] = str(wait_on_rate_limit)

    @property
    def debug(self):
        return bool(os.environ.get(self.TMDB_DEBUG_ENABLED))

    @debug.setter
    def debug(self, debug):
        os.environ[self.TMDB_DEBUG_ENABLED] = str(debug)

    @staticmethod
    def _get_obj(result, key="results"):
        if 'success' in result and result['success'] is False:
            raise Exception(result['status_message'])
        arr = []
        if key is not None:
            [arr.append(AsObj(**res)) for res in result[key]]
        else:
            return result
        return arr

    def _call(self, action, append_to_response):
        if self.api_key is None or self.api_key == '':
            raise TMDbException("No API key found.")

        url = "%s%s?api_key=%s&%s&language=%s" % (self._base, action, self.api_key, append_to_response, self.language)

        req = requests.get(url)
        headers = req.headers

        if 'X-RateLimit-Remaining' in headers:
            self._remaining = int(headers['X-RateLimit-Remaining'])

        if 'X-RateLimit-Reset' in headers:
            self._reset = int(headers['X-RateLimit-Reset'])

        if self._remaining < 1:
            current_time = int(time.time())
            sleep_time = self._reset - current_time

            if self.wait_on_rate_limit:
                logger.warning("Rate limit reached. Sleeping for: %d" % sleep_time)
                time.sleep(abs(sleep_time))
                self._call(action, append_to_response)
            else:
                raise TMDbException("Rate limit reached. Try again in %d seconds." % sleep_time)

        json = req.json()

        if 'page' in json:
            os.environ['page'] = str(json['page'])

        if 'total_results' in json:
            os.environ['total_results'] = str(json['total_results'])

        if 'total_pages' in json:
            os.environ['total_pages'] = str(json['total_pages'])

        if self.debug:
            logger.info(json)

        if 'errors' in json:
            raise TMDbException(json['errors'])

        return json
