# -*- coding: utf-8 -*-

import unittest
import util

from tmdbv3api import Find


class FindTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = util.setup()
        self.find = Find()
        
    def test_find_by_imdb_id(self):
        results = self.find.find_by_imdb_id("tt0364845")
        self.assertGreater(len(results.tv_results), 0)
        
    def test_find_by_tvdb_id(self):
        results = self.find.find_by_tvdb_id("72108")
        self.assertGreater(len(results.tv_results), 0)

    def test_find_by_freebase_mid(self):
        results = self.find.find_by_freebase_mid("/m/03m8sg")
        self.assertGreater(len(results.tv_results), 0)

    def test_find_by_freebase_id(self):
        results = self.find.find_by_freebase_id("/en/ncis")
        self.assertGreater(len(results.tv_results), 0)

    def test_find_by_tvrage_id(self):
        results = self.find.find_by_tvrage_id("4628")
        self.assertGreater(len(results.tv_results), 0)

    def test_find_by_facebook_id(self):
        results = self.find.find_by_facebook_id("NCIS")
        self.assertGreater(len(results.tv_results), 0)

    def test_find_by_instagram_id(self):
        results = self.find.find_by_instagram_id("ncis_cbs")
        self.assertGreater(len(results.tv_results), 0)

    def test_find_by_twitter_id(self):
        results = self.find.find_by_twitter_id("NCIS_CBS")
        self.assertGreater(len(results.tv_results), 0)
