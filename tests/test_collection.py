# -*- coding: utf-8 -*-

import unittest
import util

from tmdbv3api import Collection


class CollectionTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = util.setup()
        self.collection = Collection()
        self.test_collection_id = 10
         
    def test_get_collection_details(self):
        details = self.collection.details(self.test_collection_id)
        util.assertAttrs(self, details, ["id", "name", "overview", "poster_path", "backdrop_path", "parts"])
        self.assertEqual(details.id, self.test_collection_id)
        util.assertListAttrs(self, details, "parts", util.movie_attributes + ["genre_ids"])

    def test_get_collection_images(self):
        images = self.collection.images(self.test_collection_id)
        util.assertAttrs(self, images, ["id", "backdrops", "posters"])
        self.assertEqual(images.id, self.test_collection_id)
        util.assertListAttrs(self, images, "backdrops", util.image_attributes + ["iso_639_1"])
        util.assertListAttrs(self, images, "posters", util.image_attributes + ["iso_639_1"])
    
    def test_get_collection_translations(self):
        translations = self.collection.translations(self.test_collection_id)
        util.assertAttrs(self, translations, ["id", "translations"])
        self.assertEqual(translations.id, self.test_collection_id)
        util.assertListAttrs(self, translations, "translations", util.translation_attributes)
