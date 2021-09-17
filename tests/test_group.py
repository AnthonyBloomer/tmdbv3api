# -*- coding: utf-8 -*-

import unittest
import util

from tmdbv3api import Group


class GroupTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = util.setup()
        self.group = Group()
        self.test_group_id = "5b11ba820e0a265847002c6e"

    def test_get_group_details(self):
        details = self.group.details(self.test_group_id)
        util.assertAttrs(self, details, [
            "id", "description", "episode_count", "group_count", "groups", "name", "network", "type"
        ])
        self.assertEqual(details.id, self.test_group_id)
        util.assertAttrs(self, details.network, ["id", "logo_path", "name", "origin_country"])
        util.assertListAttrs(self, details, "groups", ["id", "name", "order", "episodes", "locked"])
