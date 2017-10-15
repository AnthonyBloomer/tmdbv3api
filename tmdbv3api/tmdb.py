# -*- coding: utf-8 -*-

import requests
from .endpoints import Endpoint
from .as_obj import AsObj
import os


class TMDb(object):
    def __init__(self, debug=False, language='en'):
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

    def get_config(self):
        return self._call(Endpoint.CONFIGURATION, '')

    @staticmethod
    def _get_obj(result):
        arr = []
        [arr.append(AsObj(**res)) for res in result['results']]
        return arr

    def _call(self, action, append_to_response):
        url = "%s%s?api_key=%s&%s&language=%s" % (
            Endpoint.BASE, action, self.api_key, append_to_response, self.language)

        req = requests.get(url)

        if req.status_code != 200:
            req.raise_for_status()

        json = req.json()

        if 'errors' in json:
            raise Exception(json['errors'])

        return json
