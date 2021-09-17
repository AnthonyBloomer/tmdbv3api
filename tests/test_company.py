# -*- coding: utf-8 -*-

import unittest
import util

from tmdbv3api import Company


class CompanyTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = util.setup()
        self.company = Company()
        self.test_company_id = 1

    def test_get_company_details(self):
        details = self.company.details(self.test_company_id)
        util.assertAttrs(self, details, [
            "description", "headquarters", "homepage", "id", "logo_path", "name", "origin_country", "parent_company"
        ])
        self.assertEqual(details.id, self.test_company_id)

    def test_get_company_alternative_names(self):
        alternative_names = self.company.alternative_names(self.test_company_id)
        self.assertEqual(alternative_names.id, self.test_company_id)
        util.assertListAttrs(self, alternative_names, "results", ["name", "type"])

    def test_get_company_images(self):
        images = self.company.images(self.test_company_id)
        util.assertAttrs(self, images, ["id", "logos"])
        self.assertEqual(images.id, self.test_company_id)
        util.assertListAttrs(self, images, "logos", util.image_attributes + ["id", "file_type"])

    def test_get_company_movies(self):
        movies = self.company.movies(self.test_company_id)
        util.assertAttrs(self, movies, util.pagination_attributes)
        util.assertListAttrs(self, movies, "results", util.movie_attributes)
