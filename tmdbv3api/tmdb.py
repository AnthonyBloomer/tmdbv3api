# -*- coding: utf-8 -*-

import logging
import os
import time

import requests
import requests.exceptions

from .as_obj import AsObj
from .exceptions import TMDbException

try:
    from functools import lru_cache
except ImportError:
    from backports.functools_lru_cache import lru_cache

logger = logging.getLogger(__name__)


class TMDb(object):
    _session = None
    TMDB_API_KEY = "TMDB_API_KEY"
    TMDB_LANGUAGE = "TMDB_LANGUAGE"
    TMDB_SESSION_ID = "TMDB_SESSION_ID"
    TMDB_WAIT_ON_RATE_LIMIT = "TMDB_WAIT_ON_RATE_LIMIT"
    TMDB_DEBUG_ENABLED = "TMDB_DEBUG_ENABLED"
    TMDB_CACHE_ENABLED = "TMDB_CACHE_ENABLED"
    TMDB_PROXIES = "TMDB_PROXIES"
    REQUEST_CACHE_MAXSIZE = None

    def __init__(self, obj_cached=True, session=None):
        if self.__class__._session is None or session is not None:
            self.__class__._session = requests.Session() if session is None else session
        self._base = "https://api.themoviedb.org/3"
        self._remaining = 40
        self._reset = None
        self.obj_cached = obj_cached
        if os.environ.get(self.TMDB_LANGUAGE) is None:
            os.environ[self.TMDB_LANGUAGE] = "en-US"

    @property
    def page(self):
        return os.environ["page"]

    @property
    def total_results(self):
        return os.environ["total_results"]

    @property
    def total_pages(self):
        return os.environ["total_pages"]

    @property
    def api_key(self):
        return os.environ.get(self.TMDB_API_KEY)
    
    @property
    def proxies(self):
        proxy = os.environ.get(self.TMDB_PROXIES)
        if proxy is not None:
            proxy = eval(proxy)
        return proxy

    @proxies.setter
    def proxies(self, proxies):
        if proxies is not None:
            os.environ[self.TMDB_PROXIES] = str(proxies)

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
    def has_session(self):
        return True if os.environ.get(self.TMDB_SESSION_ID) else False

    @property
    def session_id(self):
        if not os.environ.get(self.TMDB_SESSION_ID):
            raise TMDbException("Must Authenticate to create a session run Authentication(username, password)")
        return os.environ.get(self.TMDB_SESSION_ID)

    @session_id.setter
    def session_id(self, session_id):
        os.environ[self.TMDB_SESSION_ID] = session_id

    @property
    def wait_on_rate_limit(self):
        if os.environ.get(self.TMDB_WAIT_ON_RATE_LIMIT) == "False":
            return False
        else:
            return True

    @wait_on_rate_limit.setter
    def wait_on_rate_limit(self, wait_on_rate_limit):
        os.environ[self.TMDB_WAIT_ON_RATE_LIMIT] = str(wait_on_rate_limit)

    @property
    def debug(self):
        if os.environ.get(self.TMDB_DEBUG_ENABLED) == "True":
            return True
        else:
            return False

    @debug.setter
    def debug(self, debug):
        os.environ[self.TMDB_DEBUG_ENABLED] = str(debug)

    @property
    def cache(self):
        if os.environ.get(self.TMDB_CACHE_ENABLED) == "False":
            return False
        else:
            return True

    @cache.setter
    def cache(self, cache):
        os.environ[self.TMDB_CACHE_ENABLED] = str(cache)

    @staticmethod
    @lru_cache(maxsize=REQUEST_CACHE_MAXSIZE)
    def cached_request(method, url, data, json, proxies):
        return requests.request(method, url, data=data, json=json, proxies=proxies)

    def cache_clear(self):
        return self.cached_request.cache_clear()

    def _request_obj(self, action, params="", call_cached=True, method="GET", data=None, json=None, key=None):
        if self.api_key is None or self.api_key == "":
            raise TMDbException("No API key found.")

        url = "%s%s?api_key=%s&%s&language=%s" % (
            self._base,
            action,
            self.api_key,
            params,
            self.language,
        )

        if self.cache and self.obj_cached and call_cached and method != "POST":
            req = self.cached_request(method, url, data, json, self.proxies)
        else:
            req = self.__class__._session.request(method, url, data=data, json=json, proxies=self.proxies)

        headers = req.headers

        if "X-RateLimit-Remaining" in headers:
            self._remaining = int(headers["X-RateLimit-Remaining"])

        if "X-RateLimit-Reset" in headers:
            self._reset = int(headers["X-RateLimit-Reset"])

        if self._remaining < 1:
            current_time = int(time.time())
            sleep_time = self._reset - current_time

            if self.wait_on_rate_limit:
                logger.warning("Rate limit reached. Sleeping for: %d" % sleep_time)
                time.sleep(abs(sleep_time))
                return self._request_obj(action, params, call_cached, method, data, json, key)
            else:
                raise TMDbException("Rate limit reached. Try again in %d seconds." % sleep_time)

        json = req.json()

        if "page" in json:
            os.environ["page"] = str(json["page"])

        if "total_results" in json:
            os.environ["total_results"] = str(json["total_results"])

        if "total_pages" in json:
            os.environ["total_pages"] = str(json["total_pages"])

        if self.debug:
            logger.info(json)
            logger.info(self.cached_request.cache_info())

        if "errors" in json:
            raise TMDbException(json["errors"])

        if "success" in json and json["success"] is False:
            raise TMDbException(json["status_message"])

        return AsObj(json, key=key)
