# -*- coding: utf-8 -*-

import os
import unittest

from tmdbv3api import TMDb, Network


class NetworkTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = os.environ['TMDB_API_KEY']
        self.tmdb.language = "en"
        self.tmdb.debug = True
        self.tmdb.wait_on_rate_limit = True
        self.tmdb.cache = False
        self.network = Network()
        
    def test_get_network_details(self):
        network = self.network.details(1)
        self.assertTrue(hasattr(network, "name"))
        self.assertEqual(network.name, "Fuji TV")