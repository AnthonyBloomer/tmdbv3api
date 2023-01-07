# -*- coding: utf-8 -*-

import unittest
import util

from tmdbv3api import Keyword


class KeywordTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = util.setup()
        self.keyword = Keyword()
        self.test_keyword_id = 180547

    def test_get_keyword_details(self):
        details = self.keyword.details(self.test_keyword_id)
        util.assertAttrs(self, details, ["id", "name"])
        self.assertEqual(details.id, self.test_keyword_id)

    def test_get_keyword_movies(self):
        movies = self.keyword.movies(self.test_keyword_id)
        util.assertAttrs(self, movies, util.pagination_attributes)
        self.assertEqual(movies.id, self.test_keyword_id)
        util.assertListAttrs(self, movies, "results", util.movie_attributes + ["genre_ids"])
