# -*- coding: utf-8 -*-

import unittest

try:
    from unittest import mock
except ImportError:
    import mock

from tmdbv3api import TMDb, Search


EMPTY_PAGE = {"page": 1, "results": [], "total_pages": 1, "total_results": 0}


class SearchParamsTests(unittest.TestCase):
    """Offline tests that assert on the URL built for each search call."""

    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = "test_api_key"
        self.tmdb.language = "en"
        self.tmdb.cache = False
        self.response = mock.Mock(headers={})
        self.response.json.return_value = EMPTY_PAGE
        patcher = mock.patch.object(TMDb._session, "request", return_value=self.response)
        self.request = patcher.start()
        self.addCleanup(patcher.stop)
        self.search = Search()

    def called_url(self):
        return self.request.call_args[0][1]

    def test_include_adult_true(self):
        self.search.movies("matrix", adult=True)
        self.assertIn("query=matrix", self.called_url())
        self.assertIn("include_adult=true", self.called_url())

    def test_include_adult_false_keeps_query(self):
        # https://github.com/AnthonyBloomer/tmdbv3api/pull/133
        # "&include_adult=%s" % "true" if adult else "false" parses as
        # (params + "true") if adult else "false", so adult=False threw the
        # query away and sent the literal string "false" as the parameters.
        self.search.movies("matrix", adult=False)
        url = self.called_url()
        self.assertIn("query=matrix", url)
        self.assertIn("include_adult=false", url)
        self.assertNotIn("1false", url)

    def test_include_adult_omitted(self):
        self.search.movies("matrix")
        self.assertNotIn("include_adult", self.called_url())

    def test_adult_false_on_every_search(self):
        for call, term in (
            (self.search.movies, "matrix"),
            (self.search.multi, "matrix"),
            (self.search.people, "keanu"),
            (self.search.tv_shows, "breaking bad"),
        ):
            with self.subTest(call=call.__name__):
                call(term, adult=False)
                url = self.called_url()
                self.assertIn("query=", url)
                self.assertIn("include_adult=false", url)

    def test_other_filters(self):
        self.search.movies("matrix", year=1999, release_year=1999, region="US")
        url = self.called_url()
        self.assertIn("year=1999", url)
        self.assertIn("primary_release_year=1999", url)
        self.assertIn("region=US", url)


if __name__ == "__main__":
    unittest.main()
