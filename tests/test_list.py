# -*- coding: utf-8 -*-

import unittest
import util

from tmdbv3api import List
from tmdbv3api.exceptions import TMDbException


class ListTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = util.setup()
        self.list = List()
        self.test_list_id = 112870
        self.test_movie_id = 540111
        self.test_movie_id_fail = 111

    def test_get_list_details(self):
        details = self.list.details(self.test_list_id)
        util.assertAttrs(self, details, util.list_attributes + ["created_by", "items"])
        self.assertEqual(details.id, str(self.test_list_id))
        util.assertListAttrs(self, details, "items", util.movie_attributes)

    def test_get_list_check_item_status(self):
        self.list.check_item_status(self.test_list_id, self.test_movie_id)
        self.assertTrue(self.list.check_item_status(self.test_list_id, self.test_movie_id))
        self.assertFalse(self.list.check_item_status(self.test_list_id, self.test_movie_id_fail))

    def test_post_list_methods(self):
        # create_list
        list_id = self.list.create_list("Test List", "Test Description")
        self.assertGreater(int(list_id), 10)

        # add_movie
        self.list.add_movie(list_id, self.test_movie_id)
        details = self.list.details(list_id)
        self.assertEqual(details.id, str(list_id))
        self.assertEqual(details[0].id, self.test_movie_id)

        # remove_movie
        self.list.remove_movie(list_id, self.test_movie_id)
        details = self.list.details(list_id)
        self.assertEqual(len(details.items), 0)

        # clear_list
        self.list.add_movie(list_id, self.test_movie_id)
        details = self.list.details(list_id)
        self.assertEqual(details[0].id, self.test_movie_id)
        self.list.clear_list(list_id)
        details = self.list.details(list_id)
        self.assertEqual(len(details.items), 0)

        # delete_list
        try:
            self.list.delete_list(list_id)
        except TMDbException:
            pass
        self.assertRaises(TMDbException, self.list.details, list_id)
