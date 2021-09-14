# -*- coding: utf-8 -*-

import os
import unittest

from tmdbv3api import TMDb, List


class ListTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = os.environ['TMDB_API_KEY']
        self.tmdb.language = "en-US"
        self.tmdb.debug = True
        self.tmdb.wait_on_rate_limit = True
        self.tmdb.cache = False
        self.list = List()

    def test_get_list_details(self):
        list = self.list.details(112870)
        self.assertGreater(len(list.items), 10)
        self.assertTrue(hasattr(list.items[0], "id"))
        self.assertTrue(hasattr(list.items[0], "title"))