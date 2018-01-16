# -*- coding: utf-8 -*-

import requests
import requests.exceptions
import logging
from .as_obj import AsObj
import os
import time
import math

log = logging.getLogger()


class TMDb(object):
    def __init__(self, debug=False, language='en'):
        self._base = 'http://api.themoviedb.org/3'
        self._api_key = ''
        self._debug = debug
        self._language = language
        self._remaining = 40
        self._reset = None

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
            raise Exception("No API key found.")

        url = "%s%s?api_key=%s&%s&language=%s" % (self._base, action, self.api_key, append_to_response, self.language)

        req = requests.get(url)
        headers = req.headers

        if 'X-RateLimit-Remaining' in headers:
            self.remaining = int(headers['X-RateLimit-Remaining'])

        if 'X-RateLimit-Reset' in headers:
            self._reset = int(headers['X-RateLimit-Reset'])

        if self.remaining < 1:
            b = int(time.time())
            c = math.ceil(b - self._reset)
            log.warning("Rate limit reached. Sleeping for: %d" % c)
            time.sleep(c)
            self._call(action, append_to_response)

        json = req.json()

        if 'errors' in json:
            raise Exception(json['errors'])

        return json
