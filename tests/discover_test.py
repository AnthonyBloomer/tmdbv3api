# -*- coding: utf-8 -*-

import os
import unittest

from tmdbv3api import TMDb, Discover


class DiscoverTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = os.environ["TMDB_API_KEY"]
        self.tmdb.language = "en-US"
        self.tmdb.debug = True
        self.tmdb.wait_on_rate_limit = True
        self.tmdb.cache = False
        self.discover = Discover()
    
    def test_get_discover_movies(self):
        discover = self.discover.discover_movies(
            {
                "primary_release_year": "2015",
                "with_genres": "28",
                "vote_average.gte": "8",
                "page": "1"
            }
        )
        self.assertGreater(len(discover), 0)
        self.assertTrue(hasattr(discover[0], "id"))
        self.assertGreaterEqual(discover[0].vote_average, 8)
        self.assertIn(28, discover[0].genre_ids)

    def test_get_discover_tv_shows(self):
        discover = self.discover.discover_tv_shows(
            {
                "with_genres": "16", 
                "vote_average.gte": "8", 
                "page": "1"
            }
        )
        self.assertGreater(len(discover), 0)
        self.assertTrue(hasattr(discover[0], "id"))
        self.assertGreaterEqual(discover[0].vote_average, 8)
        self.assertIn(16, discover[0].genre_ids)