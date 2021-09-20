# -*- coding: utf-8 -*-

import unittest
import util

from tmdbv3api import Review


class ReviewTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = util.setup()
        self.review = Review()
        self.test_review_id = "5db0d60bcb30840013aba0d4"

    def test_get_review_details(self):
        review = self.review.details(self.test_review_id)
        util.assertAttrs(self, review, util.review_attributes + ["iso_639_1", "media_id", "media_title", "media_type"])
        self.assertEqual(review.id, self.test_review_id)
        self.assertEqual(review.media_id, 111)
