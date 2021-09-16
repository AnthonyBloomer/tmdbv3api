# -*- coding: utf-8 -*-

import os
import unittest

from tmdbv3api import TMDb, Group


class GroupTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = os.environ["TMDB_API_KEY"]
        self.tmdb.language = "en"
        self.tmdb.debug = True
        self.tmdb.wait_on_rate_limit = True
        self.tmdb.cache = False
        self.group = Group()
        self.test_group_id = "5b11ba820e0a265847002c6e"

    def test_get_group_details(self):
        details = self.group.details(self.test_group_id)
        self.assertTrue(hasattr(details, "id"))
        self.assertEqual(details.id, self.test_group_id)
        self.assertTrue(hasattr(details, "description"))
        self.assertTrue(hasattr(details, "episode_count"))
        self.assertTrue(hasattr(details, "group_count"))
        self.assertTrue(hasattr(details, "groups"))
        self.assertTrue(hasattr(details, "name"))
        self.assertTrue(hasattr(details, "network"))
        self.assertTrue(hasattr(details, "type"))
        self.assertTrue(hasattr(details.network, "id"))
        self.assertTrue(hasattr(details.network, "logo_path"))
        self.assertTrue(hasattr(details.network, "name"))
        self.assertTrue(hasattr(details.network, "origin_country"))
        self.assertGreater(len(details.groups), 0)
        self.assertTrue(hasattr(details.groups[0], "id"))
        self.assertTrue(hasattr(details.groups[0], "name"))
        self.assertTrue(hasattr(details.groups[0], "order"))
        self.assertTrue(hasattr(details.groups[0], "episodes"))
        self.assertTrue(hasattr(details.groups[0], "locked"))
