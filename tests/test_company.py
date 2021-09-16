# -*- coding: utf-8 -*-

import os
import unittest

from tmdbv3api import TMDb, Company


class CompanyTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = os.environ["TMDB_API_KEY"]
        self.tmdb.language = "en"
        self.tmdb.debug = True
        self.tmdb.wait_on_rate_limit = True
        self.tmdb.cache = False
        self.company = Company()
        self.test_company_id = 1

    def test_get_company_details(self):
        details = self.company.details(self.test_company_id)
        self.assertTrue(hasattr(details, "description"))
        self.assertTrue(hasattr(details, "headquarters"))
        self.assertTrue(hasattr(details, "homepage"))
        self.assertTrue(hasattr(details, "id"))
        self.assertTrue(hasattr(details, "logo_path"))
        self.assertTrue(hasattr(details, "name"))
        self.assertTrue(hasattr(details, "origin_country"))
        self.assertTrue(hasattr(details, "parent_company"))
        self.assertEqual(details.id, self.test_company_id)

    def test_get_company_alternative_names(self):
        alternative_names = self.company.alternative_names(self.test_company_id)
        self.assertEqual(alternative_names.id, self.test_company_id)
        self.assertGreater(len(alternative_names.results), 0)
        for alternative_name in alternative_names:
            self.assertTrue(hasattr(alternative_name, "name"))
            self.assertTrue(hasattr(alternative_name, "type"))

    def test_get_company_images(self):
        images = self.company.images(self.test_company_id)
        self.assertEqual(images.id, self.test_company_id)
        self.assertGreater(len(images.logos), 0)
        for image in images:
            self.assertTrue(hasattr(image, "aspect_ratio"))
            self.assertTrue(hasattr(image, "file_path"))
            self.assertTrue(hasattr(image, "height"))
            self.assertTrue(hasattr(image, "id"))
            self.assertTrue(hasattr(image, "file_type"))
            self.assertTrue(hasattr(image, "vote_average"))
            self.assertTrue(hasattr(image, "vote_count"))
            self.assertTrue(hasattr(image, "width"))

    def test_get_company_movies(self):
        movies = self.company.movies(self.test_company_id)
        self.assertGreater(len(movies.results), 0)
        for movie in movies:
            self.assertTrue(hasattr(movie, "id"))
            self.assertTrue(hasattr(movie, "title"))
            self.assertTrue(hasattr(movie, "overview"))
