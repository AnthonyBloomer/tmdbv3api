# -*- coding: utf-8 -*-

import util
import unittest

from tmdbv3api import Certification


class CertificationTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = util.setup()
        self.certification = Certification()

    def assert_cert(self, cert):
        util.assertListAttrs(self, cert, "certifications", ["certifications"])

    def test_get_certification_movie_list(self):
        self.assert_cert(self.certification.movie_list())

    def test_get_certification_tv_list(self):
        self.assert_cert(self.certification.tv_list())
