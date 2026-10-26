# -*- coding: utf-8 -*-

import ast
import json as json_lib
import logging
import os
import time
from urllib.parse import parse_qsl, urlencode

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
    # Bounded by default: an unbounded cache keeps every response alive for the
    # lifetime of the process. Set TMDB_REQUEST_CACHE_MAXSIZE to change it.
    REQUEST_CACHE_MAXSIZE = int(os.environ.get("TMDB_REQUEST_CACHE_MAXSIZE", 128)) or None
    DEFAULT_TIMEOUT = 30

    def __init__(self, obj_cached=True, session=None, timeout=None):
        if self.__class__._session is None or session is not None:
            self.__class__._session = requests.Session() if session is None else session
        self._base = "https://api.themoviedb.org/3"
        self._remaining = 40
        self._reset = None
        self.obj_cached = obj_cached
        self.timeout = self.DEFAULT_TIMEOUT if timeout is None else timeout
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
        if proxy is None:
            return None
        try:
            return json_lib.loads(proxy)
        except ValueError:
            # Values written by older versions were stored as str(dict).
            return ast.literal_eval(proxy)

    @proxies.setter
    def proxies(self, proxies):
        if proxies is not None:
            os.environ[self.TMDB_PROXIES] = json_lib.dumps(proxies)

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
    def cached_request(method, url, data=None, json=None, proxies=None, timeout=None):
        """Perform a request through the shared session, caching the response.

        Every argument has to be hashable, so only bodyless requests are routed
        here. ``proxies`` and ``timeout`` are passed as given by _request_obj.
        """
        return TMDb._session.request(
            method, url, data=data, json=json, proxies=proxies and dict(proxies), timeout=timeout
        )

    def cache_clear(self):
        return self.cached_request.cache_clear()

    @staticmethod
    def _as_params(params):
        """Normalise the params of a call into a list of key/value pairs.

        Accepts either a mapping or a pre-encoded query string, which is what
        the objs have always passed.
        """
        if not params:
            return []
        if isinstance(params, str):
            return parse_qsl(params, keep_blank_values=True)
        if hasattr(params, "items"):
            return list(params.items())
        return list(params)

    def _request_obj(self, action, params="", call_cached=True, method="GET", data=None, json=None, key=None):
        if self.api_key is None or self.api_key == "":
            raise TMDbException("No API key found.")

        query = [("api_key", self.api_key), ("language", self.language)]
        query += [(k, v) for k, v in self._as_params(params) if k not in ("api_key", "language")]
        url = "%s%s?%s" % (self._base, action, urlencode(query))

        cacheable = self.cache and self.obj_cached and call_cached and method != "POST" \
            and data is None and json is None
        proxies = self.proxies

        try:
            if cacheable:
                req = self.cached_request(
                    method, url, proxies=proxies and tuple(sorted(proxies.items())), timeout=self.timeout
                )
            else:
                req = self.__class__._session.request(
                    method, url, data=data, json=json, proxies=proxies, timeout=self.timeout
                )
        except requests.exceptions.RequestException as e:
            raise TMDbException("Request failed: %s" % e)

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

        try:
            json = req.json()
        except ValueError:
            raise TMDbException(
                "Could not parse the response from TMDb (HTTP %s): %s"
                % (req.status_code, req.text[:200].strip())
            )

        if isinstance(json, dict):
            if "page" in json:
                os.environ["page"] = str(json["page"])

            if "total_results" in json:
                os.environ["total_results"] = str(json["total_results"])

            if "total_pages" in json:
                os.environ["total_pages"] = str(json["total_pages"])

        if self.debug:
            logger.info(json)
            logger.info(self.cached_request.cache_info())

        if not isinstance(json, dict):
            return AsObj(json, key=key)

        if "errors" in json:
            raise TMDbException(json["errors"])

        if "success" in json and json["success"] is False:
            raise TMDbException(json["status_message"])

        return AsObj(json, key=key)
