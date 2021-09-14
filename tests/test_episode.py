# -*- coding: utf-8 -*-

import os
import unittest

from tmdbv3api import TMDb, Episode


class EpisodeTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = '48f5c3a8e871801d8ad36d4360ef1f84'
        self.tmdb.language = "en-US"
        self.tmdb.debug = True
        self.tmdb.wait_on_rate_limit = True
        self.tmdb.cache = False
        self.episode = Episode()