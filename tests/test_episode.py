# -*- coding: utf-8 -*-

import os
import unittest

from tmdbv3api import TMDb, Episode


class EpisodeTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = os.environ["TMDB_API_KEY"]
        self.tmdb.language = "en"
        self.tmdb.debug = True
        self.tmdb.wait_on_rate_limit = True
        self.tmdb.cache = False
        self.episode = Episode()
        self.test_show_id = 69050
        self.test_episode_id = 2482624
        self.test_season = 5
        self.test_episode = 1

    def test_get_episode_details(self):
        details = self.episode.details(self.test_show_id, self.test_season, self.test_episode)
        self.assertTrue(hasattr(details, "air_date"))
        self.assertTrue(hasattr(details, "crew"))
        self.assertTrue(hasattr(details, "episode_number"))
        self.assertTrue(hasattr(details, "guest_stars"))
        self.assertTrue(hasattr(details, "name"))
        self.assertTrue(hasattr(details, "overview"))
        self.assertTrue(hasattr(details, "id"))
        self.assertTrue(hasattr(details, "production_code"))
        self.assertTrue(hasattr(details, "season_number"))
        self.assertTrue(hasattr(details, "still_path"))
        self.assertTrue(hasattr(details, "vote_average"))
        self.assertTrue(hasattr(details, "vote_count"))
        self.assertEqual(details.id, self.test_episode_id)
        self.assertEqual(details.season_number, self.test_season)
        self.assertEqual(details.episode_number, self.test_episode)

    def test_get_episode_changes(self):
        changes = self.episode.changes(self.test_episode_id, start_date="2021-09-01", end_date="2021-09-14")
        self.assertTrue(hasattr(changes, "changes"))
        self.assertGreater(len(changes.changes), 0)
        for change in changes:
            self.assertTrue(hasattr(change, "key"))
            self.assertTrue(hasattr(change, "items"))

    def test_get_episode_credits(self):
        credits = self.episode.credits(self.test_show_id, self.test_season, self.test_episode)
        self.assertTrue(hasattr(credits, "id"))
        self.assertEqual(credits.id, self.test_episode_id)
        self.assertTrue(hasattr(credits, "cast"))
        self.assertTrue(hasattr(credits, "crew"))
        self.assertTrue(hasattr(credits, "guest_stars"))

    def test_get_episode_external_id(self):
        external = self.episode.external_ids(self.test_show_id, self.test_season, self.test_episode)
        self.assertTrue(hasattr(external, "id"))
        self.assertEqual(external.id, self.test_episode_id)
        self.assertTrue(hasattr(external, "imdb_id"))
        self.assertTrue(hasattr(external, "tvdb_id"))
        self.assertEqual(external.imdb_id, "tt11568508")
        self.assertEqual(external.tvdb_id, 8020104)

    def test_get_episode_images(self):
        images = self.episode.images(self.test_show_id, self.test_season, self.test_episode)
        self.assertTrue(hasattr(images, "id"))
        self.assertEqual(images.id, self.test_episode_id)
        self.assertTrue(hasattr(images, "stills"))
        self.assertGreater(len(images.stills), 0)
        self.assertTrue(hasattr(images[0], "aspect_ratio"))
        self.assertTrue(hasattr(images[0], "height"))
        self.assertTrue(hasattr(images[0], "iso_639_1"))
        self.assertTrue(hasattr(images[0], "file_path"))
        self.assertTrue(hasattr(images[0], "vote_average"))
        self.assertTrue(hasattr(images[0], "vote_count"))
        self.assertTrue(hasattr(images[0], "width"))

    def test_get_episode_translations(self):
        translations = self.episode.translations(self.test_show_id, self.test_season, self.test_episode)
        self.assertTrue(hasattr(translations, "id"))
        self.assertEqual(translations.id, self.test_episode_id)
        self.assertTrue(hasattr(translations, "translations"))
        self.assertGreater(len(translations.translations), 0)
        self.assertTrue(hasattr(translations[0], "iso_3166_1"))
        self.assertTrue(hasattr(translations[0], "iso_639_1"))
        self.assertTrue(hasattr(translations[0], "name"))
        self.assertTrue(hasattr(translations[0], "english_name"))
        self.assertTrue(hasattr(translations[0], "data"))
        self.assertTrue(hasattr(translations[0].data, "name"))
        self.assertTrue(hasattr(translations[0].data, "overview"))

    def test_get_episode_videos(self):
        videos = self.episode.videos(self.test_show_id, self.test_season, self.test_episode)
        self.assertTrue(hasattr(videos, "id"))
        self.assertEqual(videos.id, self.test_episode_id)
        self.assertTrue(hasattr(videos, "results"))
