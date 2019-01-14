# -*- coding: utf-8 -*-

import requests
import requests.exceptions
import logging
from .exceptions import TMDbException
from .as_obj import AsObj
import os
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TMDb(object):
    def __init__(self, debug=False, language='en', wait_on_rate_limit=True):
        self._base = 'http://api.themoviedb.org/3'
        self._api_key = ''
        self._debug = debug
        self._language = language
        self._remaining = 40
        self._reset = None
        self._wait_on_rate_limit = wait_on_rate_limit

    @property
    def api_key(self):
        self._api_key = os.environ.get('api_key')
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        os.environ['api_key'] = str(api_key)

    @property
    def language(self):
        self._language = os.environ.get('TMDB_LANGUAGE')
        return self._language

    @language.setter
    def language(self, language):
        os.environ['TMDB_LANGUAGE'] = language

    @property
    def debug(self):
        self._debug = os.environ.get('TMDB_DEBUG_ENABLED')
        return bool(self._debug)

    @debug.setter
    def debug(self, debug):
        os.environ['TMDB_DEBUG_ENABLED'] = str(debug)

    @staticmethod
    def _get_obj(result, key="results"):
        arr = []
        if key is not None:
            [arr.append(AsObj(**res)) for res in result[key]]
        else:
            return result
        return arr

    def _call(self, action, append_to_response):
        if self.api_key is None:
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

            if self._wait_on_rate_limit:
                logger.warning("Rate limit reached. Sleeping for: %d" % sleep_time)
                time.sleep(abs(sleep_time))
                self._call(action, append_to_response)
            else:
                raise TMDbException("Rate limit reached. Try again in %d seconds." % sleep_time)

        json = req.json()
        if self.debug:
            logger.info(json)

        if 'errors' in json:
            raise TMDbException(json['errors'])

        return json
