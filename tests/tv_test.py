# -*- coding: utf-8 -*-

import os
import unittest

from tmdbv3api import TMDb, TV


class TvTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = os.environ['TMDB_API_KEY']
        self.tmdb.language = "en"
        self.tmdb.debug = True
        self.tmdb.wait_on_rate_limit = True
        self.tmdb.cache = False
        self.tv = TV()

    def test_get_tv_repr(self):
        search = self.tv.search("Breaking Bad")
        self.assertGreater(len(search), 0)
        for result in search:
            self.assertNotEqual(str(result), "TMDB Obj")

    def test_get_tv_keywords(self):
        keywords = self.tv.keywords(1396)
        self.assertGreater(len(keywords), 0)

    def test_get_tv_reviews(self):
        reviews = self.tv.reviews(1396)
        self.assertGreater(len(reviews), 0)

    def test_get_tv_details(self):
        show = self.tv.details(12)
        self.assertIsNotNone(show)
        self.assertTrue(hasattr(show, "id"))

    def test_get_tv_on_the_air(self):
        show = self.tv.on_the_air()
        self.assertGreater(len(show), 0)

    def test_get_tv_airing_today(self):
        show = self.tv.on_the_air()
        self.assertGreater(len(show), 0)

    def test_get_tv_videos(self):
        show = self.tv.videos(1396)
        self.assertGreater(len(show), 0)

    def test_get_tv_recommendations(self):
        show = self.tv.recommendations(1396)
        self.assertGreater(len(show), 0)

    def test_get_tv_external_ids(self):
        show = self.tv.external_ids(1776)
        self.assertEqual(show["imdb_id"], "tt0488262")

    def test_get_tv_latest(self):
        latest_tv = self.tv.latest()
        self.assertIsNotNone(latest_tv)
        self.assertTrue(hasattr(latest_tv, "id"))

    def test_get_tv_search(self):
        search_tv = self.tv.search("Sunny")
        self.assertGreater(len(search_tv), 0)
        self.assertTrue(hasattr(search_tv[0], "id"))

    def test_get_tv_popular(self):
        popular = self.tv.popular()
        self.assertGreater(len(popular), 0)
        self.assertTrue(hasattr(popular[0], "id"))

    def test_get_tv_top_rated(self):
        top_rated = self.tv.top_rated()
        self.assertGreater(len(top_rated), 0)
        self.assertTrue(hasattr(top_rated[0], "id"))

    def test_get_watch_providers(self):
        watch_providers = self.tv.watch_providers(1396)
        self.assertTrue(hasattr(watch_providers, "id"))
        self.assertTrue(hasattr(watch_providers, "results"))
