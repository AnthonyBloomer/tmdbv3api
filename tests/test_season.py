# -*- coding: utf-8 -*-

import unittest
import util

from tmdbv3api import Season


class SeasonTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = util.setup()
        self.season = Season()
        self.test_tv_id = 1418
        self.test_season_id = 3738
        self.test_season = 1

    def test_get_season_details(self):
        details = self.season.details(self.test_tv_id, self.test_season)
        util.assertAttrs(self, details, [
            "_id", "air_date", "episodes", "name", "overview", "id", "poster_path", "season_number"
        ])
        self.assertEqual(details.name, "Season 1")
        self.assertEqual(details.id, self.test_season_id)
        self.assertEqual(details.season_number, self.test_season)
        util.assertListAttrs(self, details, "episodes", util.episode_attributes + ["crew", "guest_stars"])

    def test_get_season_aggregate_credits(self):
        credits = self.season.aggregate_credits(self.test_tv_id, self.test_season)
        util.assertListAttrs(self, credits, "cast", util.cast_attributes + ["total_episode_count", "roles"])
        util.assertListAttrs(self, credits, "crew", util.crew_attributes + ["total_episode_count", "jobs"])

    def test_get_season_changes(self):
        changes = self.season.changes(self.test_season_id, start_date="2021-09-01", end_date="2021-09-14")
        util.assertListAttrs(self, changes, "changes", ["key", "items"])

    def test_get_season_credits(self):
        credits = self.season.credits(self.test_tv_id, self.test_season)
        util.assertAttrs(self, credits, ["id"])
        self.assertEqual(credits.id, self.test_season_id)
        util.assertListAttrs(self, credits, "cast", util.cast_attributes + ["character"])
        util.assertListAttrs(self, credits, "crew", util.crew_attributes + ["job"])

    def test_get_season_external_ids(self):
        external = self.season.external_ids(self.test_tv_id, self.test_season)
        util.assertAttrs(self, external, ["id", "tvdb_id", "tvrage_id", "freebase_mid", "freebase_id"])
        self.assertEqual(external.id, self.test_season_id)
        self.assertEqual(external.tvdb_id, 28047)

    def test_get_season_images(self):
        images = self.season.images(self.test_tv_id, self.test_season)
        util.assertAttrs(self, images, ["id", "posters"])
        self.assertEqual(images.id, self.test_season_id)
        util.assertListAttrs(self, images, "posters", util.image_attributes + ["iso_639_1"])

    def test_get_season_translations(self):
        translations = self.season.translations(self.test_tv_id, self.test_season)
        util.assertAttrs(self, translations, ["id", "translations"])
        self.assertEqual(translations.id, self.test_season_id)
        util.assertListAttrs(self, translations, "translations", util.translation_attributes)

    def test_get_season_videos(self):
        videos = self.season.videos(self.test_tv_id, self.test_season)
        util.assertAttrs(self, videos, ["id", "results"])
        self.assertEqual(videos.id, self.test_season_id)
