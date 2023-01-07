# -*- coding: utf-8 -*-

import unittest
import util

from tmdbv3api import Genre


class GenreTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = util.setup()
        self.genre = Genre()

    def test_get_genre_movie_list(self):
        movie_genres = self.genre.movie_list()
        util.assertListAttrs(self, movie_genres, "genres", ["id", "name"])

    def test_get_genre_tv_list(self):
        tv_genres = self.genre.tv_list()
        util.assertListAttrs(self, tv_genres, "genres", ["id", "name"])
