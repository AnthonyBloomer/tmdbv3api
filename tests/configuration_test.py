# -*- coding: utf-8 -*-

import os
import unittest

from tmdbv3api import TMDb, Configuration


class ConfigurationTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = os.environ["TMDB_API_KEY"]
        self.tmdb.language = "en-US"
        self.tmdb.debug = True
        self.tmdb.wait_on_rate_limit = True
        self.tmdb.cache = False
        self.configuration = Configuration()

    def test_configuration_info(self):
        info = self.configuration.info()
        self.assertTrue(hasattr(info, "images"))
        self.assertTrue(hasattr(info, "change_keys"))
        self.assertIn("base_url", info.images)
        self.assertIn("secure_base_url", info.images)
        self.assertIn("backdrop_sizes", info.images)
        self.assertIn("logo_sizes", info.images)
        self.assertIn("poster_sizes", info.images)
        self.assertIn("profile_sizes", info.images)
        self.assertIn("still_sizes", info.images)
        

    def test_configuration_countries(self):
        countries = self.configuration.countries()
        self.assertGreater(len(countries), 0)
        for country in countries:
            self.assertIn("iso_3166_1", country)
            self.assertIn("english_name", country)

    def test_configuration_jobs(self):
        jobs = self.configuration.jobs()
        self.assertGreater(len(jobs), 0)
        for job in jobs:
            self.assertIn("department", job)
            self.assertIn("jobs", job)

    def test_configuration_languages(self):
        languages = self.configuration.languages()
        self.assertGreater(len(languages), 0)
        for language in languages:
            self.assertIn("iso_639_1", language)
            self.assertIn("english_name", language)
            self.assertIn("name", language)

    def test_configuration_primary_translations(self):
        primary_translations = self.configuration.primary_translations()
        self.assertGreater(len(primary_translations), 0)
        self.assertIn("en-US", primary_translations)
    
    def test_configuration_timezones(self):
        timezones = self.configuration.timezones()
        self.assertGreater(len(timezones), 0)
        for timezone in timezones:
            self.assertIn("iso_3166_1", timezone)
            self.assertIn("zones", timezone)