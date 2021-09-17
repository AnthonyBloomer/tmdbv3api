# -*- coding: utf-8 -*-

import unittest
import util

from tmdbv3api import Configuration


class ConfigurationTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = util.setup()
        self.configuration = Configuration()

    def test_api_configuration(self):
        info = self.configuration.api_configuration()
        util.assertAttrs(self, info, ["images", "change_keys"])
        util.assertAttrs(self, info.images, [
            "base_url", "secure_base_url", "backdrop_sizes", "logo_sizes",
            "poster_sizes", "profile_sizes", "still_sizes"
        ])

    def test_configuration_countries(self):
        countries = self.configuration.countries()
        self.assertGreater(len(countries), 0)
        for country in countries:
            util.assertAttrs(self, country, ["iso_3166_1", "english_name"])

    def test_configuration_jobs(self):
        jobs = self.configuration.jobs()
        self.assertGreater(len(jobs), 0)
        for job in jobs:
            util.assertAttrs(self, job, ["department", "jobs"])

    def test_configuration_languages(self):
        languages = self.configuration.languages()
        self.assertGreater(len(languages), 0)
        for language in languages:
            util.assertAttrs(self, language, ["iso_639_1", "english_name", "name"])

    def test_configuration_primary_translations(self):
        primary_translations = self.configuration.primary_translations()
        self.assertGreater(len(primary_translations), 0)
        self.assertIn("en-US", primary_translations)
    
    def test_configuration_timezones(self):
        timezones = self.configuration.timezones()
        self.assertGreater(len(timezones), 0)
        for timezone in timezones:
            util.assertAttrs(self, timezone, ["iso_3166_1", "zones"])
