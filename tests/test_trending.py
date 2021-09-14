# -*- coding: utf-8 -*-

import os
import unittest

from tmdbv3api import TMDb, Trending


class TrendingTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = os.environ['TMDB_API_KEY']
        self.tmdb.language = "en"
        self.tmdb.debug = True
        self.tmdb.wait_on_rate_limit = True
        self.tmdb.cache = False
        self.trending = Trending()

    def test_get_trending_all_day(self):
        trending = self.trending.all_day()
        self.assertGreater(len(trending), 0)

    def test_get_trending_all_week(self):
        trending = self.trending.all_week()
        self.assertGreater(len(trending), 0)

    def test_get_trending_movie_day(self):
        trending = self.trending.movie_day()
        self.assertGreater(len(trending), 0)

    def test_get_trending_movie_week(self):
        trending = self.trending.movie_week()
        self.assertGreater(len(trending), 0)

    def test_get_trending_tv_day(self):
        trending = self.trending.tv_day()
        self.assertGreater(len(trending), 0)

    def test_get_trending_tv_week(self):
        trending = self.trending.tv_week()
        self.assertGreater(len(trending), 0)

    def test_get_trending_person_day(self):
        trending = self.trending.person_day()
        self.assertGreater(len(trending), 0)

    def test_get_trending_person_week(self):
        trending = self.trending.person_week()
        self.assertGreater(len(trending), 0)