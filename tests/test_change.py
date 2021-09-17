# -*- coding: utf-8 -*-

import unittest
import util

from tmdbv3api import Change


class ChangesTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = util.setup()
        self.change = Change()

    def assert_changes(self, changes):
        util.assertAttrs(self, changes, util.pagination_attributes)
        util.assertAttrs(self, changes[0], ["id", "adult"])

    def test_get_changes_movie_changes(self):
        self.assert_changes(self.change.movie_change_list())

    def test_get_changes_tv_changes(self):
        self.assert_changes(self.change.tv_change_list())

    def test_get_changes_person_changes(self):
        self.assert_changes(self.change.person_change_list())
