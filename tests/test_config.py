# -*- coding: utf-8 -*-

import os
import unittest

try:
    from unittest import mock
except ImportError:
    import mock

from tmdbv3api import TMDb, Movie
from tmdbv3api.exceptions import TMDbException


class ConfigTests(unittest.TestCase):
    """Offline tests for how settings are stored and shared."""

    def setUp(self):
        self.env = dict(os.environ)
        TMDb.reset()
        self.addCleanup(TMDb.reset)
        self.addCleanup(self.restore_env)

    def restore_env(self):
        os.environ.clear()
        os.environ.update(self.env)

    def test_settings_do_not_touch_the_environment(self):
        before = dict(os.environ)
        tmdb = TMDb()
        tmdb.api_key = "test_api_key"
        tmdb.language = "fr"
        tmdb.session_id = "session"
        tmdb.debug = True
        tmdb.cache = False
        tmdb.wait_on_rate_limit = False
        tmdb.proxies = {"https": "https://proxy.example"}
        self.assertEqual(dict(os.environ), before)

    def test_settings_are_shared_between_instances(self):
        tmdb = TMDb()
        tmdb.api_key = "test_api_key"
        tmdb.language = "fr"
        movie = Movie()
        self.assertEqual(movie.api_key, "test_api_key")
        self.assertEqual(movie.language, "fr")

    def test_environment_is_used_as_a_default(self):
        os.environ["TMDB_API_KEY"] = "from_env"
        os.environ["TMDB_LANGUAGE"] = "de"
        self.assertEqual(TMDb().api_key, "from_env")
        self.assertEqual(TMDb().language, "de")

    def test_setting_overrides_the_environment(self):
        os.environ["TMDB_API_KEY"] = "from_env"
        tmdb = TMDb()
        tmdb.api_key = "explicit"
        self.assertEqual(TMDb().api_key, "explicit")

    def test_language_defaults_to_en_us(self):
        os.environ.pop("TMDB_LANGUAGE", None)
        self.assertEqual(TMDb().language, "en-US")

    def test_booleans_round_trip(self):
        tmdb = TMDb()
        self.assertTrue(tmdb.cache)
        self.assertTrue(tmdb.wait_on_rate_limit)
        self.assertFalse(tmdb.debug)
        tmdb.cache = False
        tmdb.wait_on_rate_limit = False
        tmdb.debug = True
        self.assertFalse(tmdb.cache)
        self.assertFalse(tmdb.wait_on_rate_limit)
        self.assertTrue(tmdb.debug)

    def test_booleans_read_strings_from_the_environment(self):
        os.environ["TMDB_CACHE_ENABLED"] = "False"
        os.environ["TMDB_DEBUG_ENABLED"] = "True"
        self.assertFalse(TMDb().cache)
        self.assertTrue(TMDb().debug)

    def test_session_id_requires_authentication(self):
        os.environ.pop("TMDB_SESSION_ID", None)
        tmdb = TMDb()
        self.assertFalse(tmdb.has_session)
        with self.assertRaises(TMDbException):
            tmdb.session_id
        tmdb.session_id = "session"
        self.assertTrue(tmdb.has_session)
        self.assertEqual(tmdb.session_id, "session")

    def test_pagination_properties(self):
        tmdb = TMDb()
        tmdb.api_key = "test_api_key"
        tmdb.cache = False
        self.assertIsNone(tmdb.page)
        response = mock.Mock(headers={}, status_code=200, text="")
        response.json.return_value = {"page": 2, "results": [], "total_pages": 7, "total_results": 130}
        with mock.patch.object(TMDb._session, "request", return_value=response):
            Movie().popular(page=2)
        self.assertEqual(tmdb.page, "2")
        self.assertEqual(tmdb.total_pages, "7")
        self.assertEqual(tmdb.total_results, "130")
        self.assertNotIn("page", os.environ)


if __name__ == "__main__":
    unittest.main()
