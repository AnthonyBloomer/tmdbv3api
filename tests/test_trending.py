# -*- coding: utf-8 -*-

import unittest
import util

from tmdbv3api import Trending


class TrendingTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = util.setup()
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