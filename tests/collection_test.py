# -*- coding: utf-8 -*-

import os
import unittest

from tmdbv3api import TMDb, Collection


class CollectionTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = os.environ["TMDB_API_KEY"]
        self.tmdb.language = "en"
        self.tmdb.debug = True
        self.tmdb.wait_on_rate_limit = True
        self.tmdb.cache = False
        self.collection = Collection()
         
    def test_get_collection_details(self):
        details = self.collection.details(10)
        self.assertTrue(hasattr(details, "id"))
        self.assertEqual(details.id, 10)
        self.assertTrue(hasattr(details, "name"))
        self.assertTrue(hasattr(details, "overview"))
        self.assertTrue(hasattr(details, "poster_path"))
        self.assertTrue(hasattr(details, "backdrop_path"))
        self.assertTrue(hasattr(details, "parts"))
        self.assertGreater(len(details.parts), 0)
        for movie in details.parts:
            self.assertIn("adult", movie)
            self.assertIn("backdrop_path", movie)
            self.assertIn("genre_ids", movie)
            self.assertGreater(len(movie["genre_ids"]), 0)
            self.assertIn("id", movie)
            self.assertIn("original_language", movie)
            self.assertIn("original_title", movie)
            self.assertIn("overview", movie)
            self.assertIn("release_date", movie)
            self.assertIn("poster_path", movie)
            self.assertIn("popularity", movie)
            self.assertIn("title", movie)
            self.assertIn("video", movie)
            self.assertIn("vote_average", movie)
            self.assertIn("vote_count", movie)

    def test_get_collection_images(self):
        images = self.collection.images(10)
        self.assertEqual(images.id, 10)
        self.assertTrue(hasattr(images, "backdrops"))
        self.assertTrue(hasattr(images, "posters"))
        self.assertGreater(len(images.backdrops), 0)
        self.assertGreater(len(images.posters), 0)
        for image in images.backdrops:
            self.assertIn("aspect_ratio", image)
            self.assertIn("file_path", image)
            self.assertIn("height", image)
            self.assertIn("iso_639_1", image)
            self.assertIn("vote_average", image)
            self.assertIn("vote_count", image)
            self.assertIn("width", image)
        for image in images.posters:
            self.assertIn("aspect_ratio", image)
            self.assertIn("file_path", image)
            self.assertIn("height", image)
            self.assertIn("iso_639_1", image)
            self.assertIn("vote_average", image)
            self.assertIn("vote_count", image)
            self.assertIn("width", image)
    
    def test_get_collection_translations(self):
        translations = self.collection.translations(10)
        self.assertGreater(len(translations), 0)
        for translation in translations:
            self.assertTrue(hasattr(translation, "iso_3166_1"))
            self.assertTrue(hasattr(translation, "iso_639_1"))
            self.assertTrue(hasattr(translation, "name"))
            self.assertTrue(hasattr(translation, "english_name"))
            self.assertTrue(hasattr(translation, "data"))
            self.assertIn("title", translation.data)
            self.assertIn("overview", translation.data)
            self.assertIn("homepage", translation.data)