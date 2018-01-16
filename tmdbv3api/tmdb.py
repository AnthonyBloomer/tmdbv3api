# -*- coding: utf-8 -*-

import requests
import requests.exceptions
from .as_obj import AsObj
import os
import time


class TMDb(object):
    def __init__(self, debug=False, language='en'):
        self._base = 'http://api.themoviedb.org/3'
        self._api_key = ''
        self._debug = debug
        self._language = language

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
        remaining = int(headers['X-RateLimit-Remaining'])
        reset = int(headers['X-RateLimit-Reset'])

        if remaining == 0:
            b = time.time()
            c = b - reset
            time.sleep(c)
            self._call(action, append_to_response)

        json = req.json()

        if 'errors' in json:
            raise Exception(json['errors'])

        return json
