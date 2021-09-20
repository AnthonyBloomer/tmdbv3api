# -*- coding: utf-8 -*-

import unittest
import util

from tmdbv3api import Discover


class DiscoverTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = util.setup()
        self.discover = Discover()
    
    def test_get_discover_movies(self):
        discover = self.discover.discover_movies({
            "primary_release_year": "2015",
            "with_genres": "28",
            "vote_average.gte": "8",
            "page": "1"
        })
        util.assertAttrs(self, discover, util.pagination_attributes)
        self.assertGreater(len(discover.results), 0)
        util.assertAttrs(self, discover[0], util.movie_attributes + ["genre_ids"])
        self.assertGreaterEqual(discover[0].vote_average, 8)
        self.assertIn(28, discover[0].genre_ids)

    def test_get_discover_tv_shows(self):
        discover = self.discover.discover_tv_shows({
            "with_genres": "16",
            "vote_average.gte": "8",
            "page": "1"
        })
        util.assertAttrs(self, discover, util.pagination_attributes)
        self.assertGreater(len(discover.results), 0)
        util.assertAttrs(self, discover[0], util.tv_attributes + ["genre_ids"])
        self.assertGreaterEqual(discover[0].vote_average, 8)
        self.assertIn(16, discover[0].genre_ids)
