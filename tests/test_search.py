# -*- coding: utf-8 -*-

import os
import unittest

from tmdbv3api import TMDb, Search


class SearchTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = os.environ['TMDB_API_KEY']
        self.tmdb.language = "en"
        self.tmdb.debug = True
        self.tmdb.wait_on_rate_limit = True
        self.tmdb.cache = False
        self.search = Search()

    def test_get_search_companies(self):
        search = self.search.companies("Sony")
        self.assertGreater(len(search), 0)
        self.assertTrue(hasattr(search[0], "id"))

    def test_get_search_collections(self):
        search = self.search.collections("Matrix")
        self.assertGreater(len(search), 0)
        self.assertTrue(hasattr(search[0], "id"))

    def test_get_search_keywords(self):
        search = self.search.keywords("alien")
        self.assertGreater(len(search), 0)
        self.assertTrue(hasattr(search[0], "id"))

    def test_get_search_movies(self):
        search = self.search.movies("Matrix", year=1999)
        self.assertGreater(len(search), 0)
        self.assertTrue(hasattr(search[0], "id"))

    def test_get_search_multi(self):
        search = self.search.multi("Will")
        self.assertGreater(len(search), 0)
        self.assertTrue(hasattr(search[0], "id"))

    def test_get_search_people(self):
        search = self.search.people("Will Smith")
        self.assertGreater(len(search), 0)
        self.assertTrue(hasattr(search[0], "id"))

    def test_get_search_tv_shows(self):
        search = self.search.tv_shows("Breaking Bad")
        self.assertGreater(len(search), 0)
        self.assertTrue(hasattr(search[0], "id"))