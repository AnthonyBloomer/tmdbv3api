# -*- coding: utf-8 -*-

import unittest
import util

from tmdbv3api import Episode


class EpisodeTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = util.setup()
        self.episode = Episode()
        self.test_show_id = 69050
        self.test_episode_id = 2482624
        self.test_season = 5
        self.test_episode = 1

    def test_get_episode_details(self):
        details = self.episode.details(self.test_show_id, self.test_season, self.test_episode)
        util.assertAttrs(self, details, util.episode_attributes + ["crew", "guest_stars"])
        self.assertEqual(details.id, self.test_episode_id)
        self.assertEqual(details.season_number, self.test_season)
        self.assertEqual(details.episode_number, self.test_episode)

    def test_get_episode_changes(self):
        changes = self.episode.changes(self.test_episode_id, start_date="2021-09-01", end_date="2021-09-14")
        util.assertListAttrs(self, changes, "changes", ["key", "items"])

    def test_get_episode_credits(self):
        credits = self.episode.credits(self.test_show_id, self.test_season, self.test_episode)
        util.assertAttrs(self, credits, ["id", "cast", "crew", "guest_stars"])
        self.assertEqual(credits.id, self.test_episode_id)

    def test_get_episode_external_id(self):
        external = self.episode.external_ids(self.test_show_id, self.test_season, self.test_episode)
        util.assertAttrs(self, external, ["id", "imdb_id", "tvdb_id", "tvrage_id", "freebase_mid", "freebase_id"])
        self.assertEqual(external.id, self.test_episode_id)
        self.assertEqual(external.imdb_id, "tt11568508")
        self.assertEqual(external.tvdb_id, 8020104)

    def test_get_episode_images(self):
        images = self.episode.images(self.test_show_id, self.test_season, self.test_episode)
        util.assertAttrs(self, images, ["id", "stills"])
        self.assertEqual(images.id, self.test_episode_id)
        util.assertListAttrs(self, images, "stills", util.image_attributes + ["iso_639_1"])

    def test_get_episode_translations(self):
        translations = self.episode.translations(self.test_show_id, self.test_season, self.test_episode)
        util.assertAttrs(self, translations, ["id", "translations"])
        self.assertEqual(translations.id, self.test_episode_id)
        util.assertListAttrs(self, translations, "translations", util.translation_attributes)

    def test_get_episode_videos(self):
        videos = self.episode.videos(self.test_show_id, self.test_season, self.test_episode)
        util.assertAttrs(self, videos, ["id", "results"])
        self.assertEqual(videos.id, self.test_episode_id)
