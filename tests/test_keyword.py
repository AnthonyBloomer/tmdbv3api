# -*- coding: utf-8 -*-

import os
import unittest

from tmdbv3api import TMDb, Keyword


class KeywordTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = os.environ['TMDB_API_KEY']
        self.tmdb.language = "en"
        self.tmdb.debug = True
        self.tmdb.wait_on_rate_limit = True
        self.tmdb.cache = False
        self.keyword = Keyword()

    def test_get_keyword_details(self):
        details = self.keyword.details(180547)
        self.assertTrue(hasattr(details, "name"))

    def test_get_keyword_movies(self):
        movies = self.keyword.movies(180547)
        self.assertGreater(len(movies), 0)
        for movie in  movies:
            self.assertTrue(hasattr(movie, "title"))
            self.assertTrue(hasattr(movie, "overview"))