# -*- coding: utf-8 -*-

import os
import unittest

from tmdbv3api import TMDb, Certification


class CertificationTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = os.environ["TMDB_API_KEY"]
        self.tmdb.language = "en-US"
        self.tmdb.debug = True
        self.tmdb.wait_on_rate_limit = True
        self.tmdb.cache = False
        self.certification = Certification()
         
    def test_get_certification_movie_list(self):
        movie_certifications = self.certification.movie_list()
        self.assertTrue(hasattr(movie_certifications, "certifications"))

    def test_get_certification_tv_list(self):
        tv_certifications = self.certification.tv_list()
        self.assertTrue(hasattr(tv_certifications, "certifications"))
    