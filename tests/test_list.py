# -*- coding: utf-8 -*-

import os
import unittest

from tmdbv3api import TMDb, List, Authentication
from tmdbv3api.exceptions import TMDbException


class ListTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = os.environ['TMDB_API_KEY']
        self.tmdb.language = "en-US"
        self.tmdb.debug = True
        self.tmdb.wait_on_rate_limit = True
        self.tmdb.cache = False
        self.auth = Authentication(os.environ['TMDB_USERNAME'], os.environ['TMDB_PASSWORD'])
        self.list = List()

    def test_get_list_details(self):
        details = self.list.details(112870)
        self.assertEqual(details.id, "112870")
        self.assertGreater(len(details), 10)
        self.assertTrue(hasattr(details[0], "id"))
        self.assertTrue(hasattr(details[0], "title"))

    def test_get_list_check_item_status(self):
        self.list.check_item_status(112870, 540111)
        self.assertTrue(self.list.check_item_status(112870, 540111))
        self.assertFalse(self.list.check_item_status(112870, 111))

    def test_post_list_methods(self):
        # create_list
        list_id = self.list.create_list("Test List", "Test Description")
        self.assertGreater(int(list_id), 10)

        # add_movie
        self.list.add_movie(list_id, 540111)
        details = self.list.details(list_id)
        self.assertEqual(details.id, str(list_id))
        self.assertEqual(details[0].id, 540111)

        # remove_movie
        self.list.remove_movie(list_id, 540111)
        details = self.list.details(list_id)
        self.assertEqual(len(details.items), 0)

        # clear_list
        self.list.add_movie(list_id, 540111)
        details = self.list.details(list_id)
        self.assertEqual(details[0].id, 540111)
        self.list.clear_list(list_id)
        details = self.list.details(list_id)
        self.assertEqual(len(details.items), 0)

        # delete_list
        try:
            self.list.delete_list(list_id)
        except TMDbException:
            pass
        self.assertRaises(TMDbException, self.list.details, list_id)
