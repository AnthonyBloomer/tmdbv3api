# -*- coding: utf-8 -*-

import unittest
import util

from tmdbv3api import Credit


class CreditsTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = util.setup()
        self.credit = Credit()
        self.test_credit_id = "52542282760ee313280017f9"

    def test_get_credit_details(self):
        credit = self.credit.details(self.test_credit_id)
        util.assertAttrs(self, credit, ["credit_type", "department", "job", "media", "media_type", "id", "person"])
        self.assertEqual(credit.id, self.test_credit_id)
        util.assertAttrs(self, credit.media, ["id", "name"])
        util.assertAttrs(self, credit.person, ["id", "name"])
