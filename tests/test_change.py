# -*- coding: utf-8 -*-

import unittest
import assert_helper

from tmdbv3api import Change


class ChangesTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = assert_helper.setup()
        self.change = Change()

    def test_get_changes_movie_changes(self):
        assert_helper.assert_pagination(self, self.change.movie_change_list())

    def test_get_changes_tv_changes(self):
        assert_helper.assert_pagination(self, self.change.tv_change_list())

    def test_get_changes_person_changes(self):
        assert_helper.assert_pagination(self, self.change.person_change_list())
