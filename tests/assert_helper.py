import os

from tmdbv3api import TMDb


def setup():
    tmdb = TMDb()
    tmdb.api_key = os.environ["TMDB_API_KEY"]
    tmdb.language = "en"
    tmdb.debug = True
    tmdb.wait_on_rate_limit = True
    tmdb.cache = False
    return tmdb


def assert_pagination(test, items):
    test.assertTrue(hasattr(items, "page"))
    test.assertTrue(hasattr(items, "total_pages"))
    test.assertTrue(hasattr(items, "total_results"))
    test.assertTrue(hasattr(items, "results"))
    test.assertGreater(len(items.results), 0)