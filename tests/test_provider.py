# -*- coding: utf-8 -*-

import unittest
import util

from tmdbv3api import Provider


class ProviderTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = util.setup()
        self.provider = Provider()

    def test_get_provider_available_regions(self):
        provider = self.provider.available_regions()
        util.assertListAttrs(self, provider, "results", ["iso_3166_1", "english_name", "native_name"])

    def test_get_provider_movie_providers(self):
        provider = self.provider.movie_providers()
        util.assertListAttrs(self, provider, "results", [
            "display_priority", "logo_path", "provider_name", "provider_id"
        ])

    def test_get_provider_tv_providers(self):
        provider = self.provider.tv_providers()
        util.assertListAttrs(self, provider, "results", [
            "display_priority", "logo_path", "provider_name", "provider_id"
        ])
