# -*- coding: utf-8 -*-

import os
import unittest

from tmdbv3api import TMDb, Genre


class GenreTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = os.environ['TMDB_API_KEY']
        self.tmdb.language = "en-US"
        self.tmdb.debug = True
        self.tmdb.wait_on_rate_limit = True
        self.tmdb.cache = False
        self.genre = Genre()

    def test_get_genre_movie_list(self):
        movie_genres = self.genre.movie_list()
        self.assertGreater(len(movie_genres), 0)

    def test_get_genre_tv_list(self):
        tv_genres = self.genre.tv_list()
        self.assertGreater(len(tv_genres), 0)  