# -*- coding: utf-8 -*-

import unittest
import util

from tmdbv3api import Person


class PersonTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = util.setup()
        self.person = Person()
        self.test_person_id = 2888

    def test_get_person_details(self):
        details = self.person.details(self.test_person_id)
        util.assertAttrs(self, details, util.all_person_attributes + ["known_for_department"])
        self.assertEqual(details.id, self.test_person_id)

    def asset_changes(self, changes):
        util.assertAttrs(self, changes, ["changes"])
        util.assertListAttrs(self, changes, "changes", ["key", "items"])

    def test_get_person_changes(self):
        self.asset_changes(self.person.changes(self.test_person_id, start_date="2021-03-10", end_date="2021-03-15"))
        self.asset_changes(self.person.changes(self.test_person_id, start_date="2021-03-10"))
        self.asset_changes(self.person.changes(self.test_person_id, end_date="2021-03-15"))

    def assert_credits(self, credits):
        util.assertAttrs(self, credits, ["id", "cast", "crew"])
        self.assertEqual(credits.id, self.test_person_id)

    def test_get_person_movie_credits(self):
        self.assert_credits(self.person.movie_credits(self.test_person_id))

    def test_get_person_tv_credits(self):
        self.assert_credits(self.person.tv_credits(self.test_person_id))

    def test_get_person_combined_credits(self):
        self.assert_credits(self.person.combined_credits(self.test_person_id))

    def test_get_person_external_ids(self):
        external = self.person.external_ids(self.test_person_id)
        util.assertAttrs(self, external, ["id", "freebase_mid", "freebase_id", "imdb_id", "tvrage_id", "facebook_id", "instagram_id", "twitter_id"])
        self.assertEqual(external.id, self.test_person_id)
        self.assertEqual(external.imdb_id, "nm0000226")

    def test_get_person_images(self):
        images = self.person.images(self.test_person_id)
        util.assertAttrs(self, images, ["id"])
        self.assertEqual(images.id, self.test_person_id)
        util.assertListAttrs(self, images, "profiles", util.image_attributes + ["iso_639_1"])

    def test_get_person_tagged_images(self):
        images = self.person.tagged_images(self.test_person_id)
        util.assertAttrs(self, images, util.pagination_attributes)
        util.assertListAttrs(self, images, "results", util.image_attributes + ["iso_639_1"])

    def test_get_person_translations(self):
        translations = self.person.translations(self.test_person_id)
        util.assertAttrs(self, translations, ["id", "translations"])
        self.assertEqual(translations.id, self.test_person_id)
        util.assertListAttrs(self, translations, "translations", util.translation_attributes)

    def test_get_person_latest(self):
        latest = self.person.latest()
        util.assertAttrs(self, latest, util.all_person_attributes)

    def test_get_person_popular(self):
        popular = self.person.popular()
        util.assertAttrs(self, popular, util.pagination_attributes)
        self.assertTrue(len(popular.results) > 0)
        util.assertAttrs(self, popular.results[0], util.person_attributes + ["known_for", "known_for_department"])

