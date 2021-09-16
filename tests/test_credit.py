# -*- coding: utf-8 -*-

import os
import unittest

from tmdbv3api import TMDb, Credit


class CreditsTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = os.environ["TMDB_API_KEY"]
        self.tmdb.language = "en"
        self.tmdb.debug = True
        self.tmdb.wait_on_rate_limit = True
        self.tmdb.cache = False
        self.credit = Credit()
        self.test_credit_id = "52542282760ee313280017f9"

    def test_get_credit_details(self):
        credit = self.credit.details(self.test_credit_id)
        self.assertTrue(hasattr(credit, "credit_type"))
        self.assertTrue(hasattr(credit, "department"))
        self.assertTrue(hasattr(credit, "job"))
        self.assertTrue(hasattr(credit, "media"))
        self.assertTrue(hasattr(credit, "media_type"))
        self.assertTrue(hasattr(credit, "id"))
        self.assertTrue(hasattr(credit, "person"))
        self.assertEqual(credit.id, self.test_credit_id)
        self.assertTrue(hasattr(credit.media, "id"))
        self.assertTrue(hasattr(credit.media, "name"))
        self.assertTrue(hasattr(credit.person, "name"))
        self.assertTrue(hasattr(credit.person, "id"))
