# -*- coding: utf-8 -*-

import os
import unittest

from tmdbv3api import TMDb, Person


class PersonTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = os.environ['TMDB_API_KEY']
        self.tmdb.language = "en"
        self.tmdb.debug = True
        self.tmdb.wait_on_rate_limit = True
        self.tmdb.cache = False
        self.person = Person()

    def test_get_person(self):
        person = self.person.details(234)
        self.assertIsNotNone(person)
        self.assertTrue(hasattr(person, "id"))

    def test_get_person_search(self):
        search_person = self.person.search("Bryan")
        self.assertIsNotNone(search_person)
        self.assertGreater(len(search_person), 0)
        for person in search_person:
            self.assertTrue(hasattr(person, "id"))

    def test_get_person_popular(self):
        popular = self.person.popular()
        self.assertTrue(len(popular) > 0)
        first = popular[0]
        self.assertTrue(hasattr(first, "name"))
        self.assertTrue(hasattr(first, "known_for"))

    def test_get_person_latest(self):
        latest = self.person.latest()
        self.assertIsNotNone(latest)
        self.assertTrue(hasattr(latest, "name"))
        self.assertTrue(hasattr(latest, "id"))

    def test_get_person_images(self):
        images = self.person.images(11)
        self.assertIsNotNone(images)
        self.assertTrue(hasattr(images, "profiles"))
        self.assertTrue(hasattr(images, "id"))