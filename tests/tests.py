# -*- coding: utf-8 -*-

import unittest
from tmdbv3api import TMDb


class TMDbTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb('')

    def test_search(self):
        movie = self.tmdb.search("Pokémon")
        for l in movie:
            print l.title

