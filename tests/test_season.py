# -*- coding: utf-8 -*-

import os
import unittest

from tmdbv3api import TMDb, Season


class SeasonTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = os.environ['TMDB_API_KEY']
        self.tmdb.language = "en"
        self.tmdb.debug = True
        self.tmdb.wait_on_rate_limit = True
        self.tmdb.cache = False
        self.season = Season()

    def test_get_season(self):
        season = self.season.details(1418, 1)
        self.assertIsNotNone(season)
        self.assertEqual(season.name, "Season 1")
        self.assertEqual(season.id, 3738)
        self.assertTrue(hasattr(season, "episodes"))
        self.assertTrue(hasattr(season, "overview"))
        self.assertTrue(hasattr(season, "id"))

    def test_get_season_changes(self):
        changes = self.season.changes(1418)
        self.assertIsNotNone(changes)

    def test_get_season_external_ids(self):
        external_ids = self.season.external_ids(1418, 1)
        self.assertIsNotNone(external_ids)
        self.assertIn("tvdb_id", external_ids)

    def test_get_season_videos(self):
        videos = self.season.videos(1418, 1)

    def test_get_season_images(self):
        images = self.season.images(1418, 1)
        for image in images:
            self.assertTrue(hasattr(image, "width"))
            self.assertTrue(hasattr(image, "height"))

    def test_get_season_credits(self):
        credits = self.season.credits(1418, 1)
        self.assertIn("cast", credits)
        self.assertTrue(hasattr(credits, "crew"))
        self.assertTrue(hasattr(credits, "id"))
        for person in credits.cast:
            self.assertTrue(hasattr(person, "name"))
            self.assertTrue(hasattr(person, "character"))
        for person in credits.crew:
            self.assertTrue(hasattr(person, "name"))
            self.assertTrue(hasattr(person, "department"))