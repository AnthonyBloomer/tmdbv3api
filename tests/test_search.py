# -*- coding: utf-8 -*-

import unittest
import util

from tmdbv3api import Search


class SearchTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = util.setup()
        self.search = Search()

    def assert_search(self, search):
        util.assertAttrs(self, search, util.pagination_attributes)
        self.assertGreater(len(search.results), 0)
        self.assertTrue(hasattr(search.results[0], "id"))

    def test_get_search_companies(self):
        self.assert_search(self.search.companies("Sony"))

    def test_get_search_collections(self):
        self.assert_search(self.search.collections("Matrix"))

    def test_get_search_keywords(self):
        self.assert_search(self.search.keywords("alien"))

    def test_get_search_movies(self):
        self.assert_search(self.search.movies("Matrix", year=1999))

    def test_get_search_multi(self):
        self.assert_search(self.search.multi("Will"))

    def test_get_search_people(self):
        self.assert_search(self.search.people("Will Smith"))

    def test_get_search_tv_shows(self):
        self.assert_search(self.search.tv_shows("Breaking Bad"))