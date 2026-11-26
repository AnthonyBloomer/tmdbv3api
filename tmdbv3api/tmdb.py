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
    # Settings are shared by every TMDb instance in the process, so that the
    # documented usage of configuring one TMDb() and then constructing Movie(),
    # TV() and friends keeps working. Environment variables seed the defaults.
    _settings = {}
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

    @classmethod
    def _setting(cls, name, env_var, default=None):
        """Read a setting, falling back to its environment variable."""
        if name in cls._settings:
            return cls._settings[name]
        value = os.environ.get(env_var)
        return default if value is None else value

    @classmethod
    def reset(cls):
        """Forget every setting configured at runtime."""
        cls._settings.clear()

    @property
    def page(self):
        return self._settings.get("page")

    @property
    def total_results(self):
        return self._settings.get("total_results")

    @property
    def total_pages(self):
        return self._settings.get("total_pages")

    @property
    def api_key(self):
        return self._setting("api_key", self.TMDB_API_KEY)

    @api_key.setter
    def api_key(self, api_key):
        self._settings["api_key"] = str(api_key)

    @property
    def proxies(self):
        proxies = self._setting("proxies", self.TMDB_PROXIES)
        if proxies is None or isinstance(proxies, dict):
            return proxies
        try:
            return json_lib.loads(proxies)
        except ValueError:
            # Values written by older versions were stored as str(dict).
            return ast.literal_eval(proxies)

    @proxies.setter
    def proxies(self, proxies):
        if proxies is not None:
            self._settings["proxies"] = proxies

    @property
    def language(self):
        return self._setting("language", self.TMDB_LANGUAGE, default="en-US")

    @language.setter
    def language(self, language):
        self._settings["language"] = language

    @property
    def has_session(self):
        return bool(self._setting("session_id", self.TMDB_SESSION_ID))

    @property
    def session_id(self):
        session_id = self._setting("session_id", self.TMDB_SESSION_ID)
        if not session_id:
            raise TMDbException("Must Authenticate to create a session run Authentication(username, password)")
        return session_id

    @session_id.setter
    def session_id(self, session_id):
        self._settings["session_id"] = session_id

    @property
    def wait_on_rate_limit(self):
        return self._as_bool(self._setting("wait_on_rate_limit", self.TMDB_WAIT_ON_RATE_LIMIT), default=True)

    @wait_on_rate_limit.setter
    def wait_on_rate_limit(self, wait_on_rate_limit):
        self._settings["wait_on_rate_limit"] = bool(wait_on_rate_limit)

    @property
    def debug(self):
        return self._as_bool(self._setting("debug", self.TMDB_DEBUG_ENABLED), default=False)

    @debug.setter
    def debug(self, debug):
        self._settings["debug"] = bool(debug)

    @property
    def cache(self):
        return self._as_bool(self._setting("cache", self.TMDB_CACHE_ENABLED), default=True)

    @cache.setter
    def cache(self, cache):
        self._settings["cache"] = bool(cache)

    @staticmethod
    def _as_bool(value, default):
        if value is None:
            return default
        if isinstance(value, bool):
            return value
        return str(value).strip().lower() not in ("false", "0", "no", "")

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
            # Kept for backwards compatibility. Prefer reading these off the
            # response itself, which is correct when requests overlap.
            for field in ("page", "total_results", "total_pages"):
                if field in json:
                    self._settings[field] = str(json[field])

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
