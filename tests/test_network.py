# -*- coding: utf-8 -*-

import unittest
import util

from tmdbv3api import Network


class NetworkTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = util.setup()
        self.network = Network()
        self.test_network_id = 1
        
    def test_get_network_details(self):
        network = self.network.details(self.test_network_id)
        util.assertAttrs(self, network, ["headquarters", "homepage", "id", "logo_path", "name", "origin_country"])
        self.assertEqual(network.name, "Fuji TV")

    def test_get_network_alternative_names(self):
        alternative_names = self.network.alternative_names(self.test_network_id)
        util.assertAttrs(self, alternative_names, ["id", "results"])
        self.assertEqual(alternative_names.id, self.test_network_id)
        util.assertListAttrs(self, alternative_names, "results", ["name", "type"])

    def test_get_network_images(self):
        images = self.network.images(self.test_network_id)
        util.assertAttrs(self, images, ["id"])
        self.assertEqual(images.id, self.test_network_id)
        util.assertListAttrs(self, images, "logos", util.image_attributes + ["file_type"])