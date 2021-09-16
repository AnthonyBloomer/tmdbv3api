# -*- coding: utf-8 -*-

import os
import unittest

from tmdbv3api import TMDb, Keyword


class KeywordTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = os.environ["TMDB_API_KEY"]
        self.tmdb.language = "en"
        self.tmdb.debug = True
        self.tmdb.wait_on_rate_limit = True
        self.tmdb.cache = False
        self.keyword = Keyword()
        self.test_keyword_id = 180547

    def test_get_keyword_details(self):
        details = self.keyword.details(self.test_keyword_id)
        self.assertEqual(details.id, self.test_keyword_id)
        self.assertTrue(hasattr(details, "name"))

    def test_get_keyword_movies(self):
        movies = self.keyword.movies(self.test_keyword_id)
        self.assertEqual(movies.id, self.test_keyword_id)
        self.assertGreater(len(movies.results), 0)
        for movie in movies:
            self.assertTrue(hasattr(movie, "title"))
            self.assertTrue(hasattr(movie, "overview"))
