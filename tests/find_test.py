# -*- coding: utf-8 -*-

import os
import unittest

from tmdbv3api import TMDb, Find


class FindTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = os.environ['TMDB_API_KEY']
        self.tmdb.language = "en-US"
        self.tmdb.debug = True
        self.tmdb.wait_on_rate_limit = True
        self.tmdb.cache = False
        self.find = Find()
        
    def test_find_by_imdb_id(self):
        results = self.Find().find_by_imdb_id("tt0076759")
        self.assertGreater(len(results["movie_results"]), 0)
        
    def test_find_by_tvdb_id(self):
        results = self.Find().find_by_tvdb_id("83268")
        self.assertGreater(len(results["tv_results"]), 0)