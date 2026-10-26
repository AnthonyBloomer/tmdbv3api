# -*- coding: utf-8 -*-

import os
import unittest
from urllib.parse import parse_qs, urlparse

try:
    from unittest import mock
except ImportError:
    import mock

import requests

from tmdbv3api import TMDb, Movie
from tmdbv3api.exceptions import TMDbException


MOVIE = {"id": 343611, "title": "Jack Reacher: Never Go Back"}


class RequestTests(unittest.TestCase):
    """Offline tests for the HTTP layer in TMDb._request_obj."""

    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = "test_api_key"
        self.tmdb.language = "en"
        self.tmdb.cache = False
        self.tmdb.wait_on_rate_limit = False
        self.response = mock.Mock(headers={}, status_code=200, text="")
        self.response.json.return_value = MOVIE
        patcher = mock.patch.object(TMDb._session, "request", return_value=self.response)
        self.request = patcher.start()
        self.addCleanup(patcher.stop)
        self.addCleanup(self.tmdb.cache_clear)

    def query(self):
        return parse_qs(urlparse(self.request.call_args[0][1]).query)

    def test_query_string_is_well_formed(self):
        Movie().details(343611)
        url = self.request.call_args[0][1]
        self.assertNotIn("&&", url)
        self.assertNotIn("?&", url)
        query = self.query()
        self.assertEqual(query["api_key"], ["test_api_key"])
        self.assertEqual(query["language"], ["en"])
        self.assertIn("append_to_response", query)

    def test_params_accepts_a_mapping(self):
        self.tmdb._request_obj("/movie/343611", params={"append_to_response": "videos"})
        self.assertEqual(self.query()["append_to_response"], ["videos"])

    def test_params_cannot_override_credentials(self):
        self.tmdb._request_obj("/movie/343611", params="api_key=leaked&language=de")
        query = self.query()
        self.assertEqual(query["api_key"], ["test_api_key"])
        self.assertEqual(query["language"], ["en"])

    def test_values_are_encoded_once(self):
        self.tmdb._request_obj("/search/movie", params={"query": "l'été meurtrier"})
        self.assertEqual(self.query()["query"], ["l'été meurtrier"])

    def test_timeout_is_passed(self):
        Movie().details(343611)
        self.assertEqual(self.request.call_args[1]["timeout"], TMDb.DEFAULT_TIMEOUT)

    def test_timeout_is_configurable(self):
        tmdb = TMDb(timeout=5)
        tmdb._request_obj("/movie/343611")
        self.assertEqual(self.request.call_args[1]["timeout"], 5)

    def test_non_json_response_raises_tmdb_exception(self):
        self.response.json.side_effect = ValueError("no json")
        self.response.status_code = 503
        self.response.text = "<html>Service Unavailable</html>"
        with self.assertRaises(TMDbException) as ctx:
            Movie().details(343611)
        self.assertIn("503", str(ctx.exception))

    def test_connection_error_raises_tmdb_exception(self):
        self.request.side_effect = requests.exceptions.ConnectTimeout("timed out")
        with self.assertRaises(TMDbException):
            Movie().details(343611)

    def test_post_body_is_not_cached(self):
        self.tmdb.cache = True
        self.tmdb._request_obj("/list/1/add_item", method="POST", json={"media_id": 1})
        self.assertEqual(self.request.call_args[1]["json"], {"media_id": 1})

    def test_get_with_a_body_is_not_cached(self):
        # lru_cache raises TypeError on dict arguments, so bodies bypass it.
        self.tmdb.cache = True
        self.tmdb._request_obj("/movie/343611", json={"a": 1})
        self.assertEqual(self.request.call_args[1]["json"], {"a": 1})

    def test_cached_requests_use_the_session(self):
        self.tmdb.cache = True
        self.tmdb._request_obj("/movie/343611")
        self.tmdb._request_obj("/movie/343611")
        self.assertEqual(self.request.call_count, 1)

    def test_proxies_are_not_evaluated(self):
        self.addCleanup(os.environ.pop, TMDb.TMDB_PROXIES, None)
        self.tmdb.proxies = {"https": "https://proxy.example"}
        self.assertEqual(self.tmdb.proxies, {"https": "https://proxy.example"})
        Movie().details(343611)
        self.assertEqual(self.request.call_args[1]["proxies"], {"https": "https://proxy.example"})

    def test_list_responses_are_returned(self):
        self.response.json.return_value = [{"iso_3166_1": "US"}]
        result = self.tmdb._request_obj("/configuration/countries")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["iso_3166_1"], "US")


if __name__ == "__main__":
    unittest.main()
