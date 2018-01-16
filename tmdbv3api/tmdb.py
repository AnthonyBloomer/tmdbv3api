# -*- coding: utf-8 -*-

import requests
import requests.exceptions
import logging
from .exceptions import TMDbException, ApiException
from .as_obj import AsObj
import os
import time

log = logging.getLogger()


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
    def debug(self):
        return self._debug

    @debug.setter
    def debug(self, debug):
        self._debug = debug

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, language):
        self._language = language

    @staticmethod
    def _get_obj(result, key="results"):
        arr = []
        [arr.append(AsObj(**res)) for res in result[key]]
        return arr

    def _call(self, action, append_to_response):
        if self.api_key is None:
            raise ApiException("No API key found.")

        url = "%s%s?api_key=%s&%s&language=%s" % (self._base, action, self.api_key, append_to_response, self.language)

        req = requests.get(url)
        headers = req.headers

        if 'X-RateLimit-Remaining' in headers:
            self._remaining = int(headers['X-RateLimit-Remaining'])

        if 'X-RateLimit-Reset' in headers:
            self._reset = int(headers['X-RateLimit-Reset'])

        if self._remaining < 1:
            b = int(time.time())
            c = self._reset - b

            if self._wait_on_rate_limit:
                log.warning("Rate limit reached. Sleeping for: %d" % c)
                time.sleep(c)
                self._call(action, append_to_response)
            else:
                raise TMDbException("Rate limit reached. Try again in %d seconds." % c)

        json = req.json()

        if 'status_code' in json and int(json['status_code']) == 7:
            raise ApiException("Invalid API key: You must be granted a valid key.")
        if 'errors' in json:
            raise TMDbException(json['errors'])

        return json
