# -*- coding: utf-8 -*-

import unittest
import util

from tmdbv3api import TV


class TvTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = util.setup()
        self.tv = TV()
        self.test_tv_id = 1396
        self.test2_tv_id = 46638
        self.test3_tv_id = 4194

    def test_get_tv_details(self):
        details = self.tv.details(self.test_tv_id)
        util.assertAttrs(self, details, util.tv_attributes + ["genres"])
        self.assertEqual(details.id, self.test_tv_id)

    def test_get_tv_aggregate_credits(self):
        credits = self.tv.aggregate_credits(self.test_tv_id)
        util.assertListAttrs(self, credits, "cast", util.cast_attributes + ["total_episode_count", "roles"])
        util.assertListAttrs(self, credits, "crew", util.crew_attributes + ["total_episode_count", "jobs"])

    def test_get_tv_alternative_titles(self):
        alternative_titles = self.tv.alternative_titles(self.test_tv_id)
        util.assertAttrs(self, alternative_titles, ["id"])
        self.assertEqual(alternative_titles.id, self.test_tv_id)
        util.assertListAttrs(self, alternative_titles, "results", util.alt_titles_attributes)

    def asset_changes(self, changes):
        util.assertAttrs(self, changes, ["changes"])
        util.assertListAttrs(self, changes, "changes", ["key", "items"])

    def test_get_tv_changes(self):
        self.asset_changes(self.tv.changes(self.test_tv_id, start_date="2021-09-01", end_date="2021-09-14"))
        self.asset_changes(self.tv.changes(self.test_tv_id, start_date="2021-09-01"))
        self.asset_changes(self.tv.changes(self.test_tv_id, end_date="2021-09-14"))

    def test_get_tv_content_ratings(self):
        content_ratings = self.tv.content_ratings(self.test_tv_id)
        util.assertAttrs(self, content_ratings, ["id"])
        self.assertEqual(content_ratings.id, self.test_tv_id)
        util.assertListAttrs(self, content_ratings, "results", ["iso_3166_1", "rating"])

    def test_get_tv_credits(self):
        credits = self.tv.credits(self.test_tv_id)
        util.assertAttrs(self, credits, ["id"])
        self.assertEqual(credits.id, self.test_tv_id)
        util.assertListAttrs(self, credits, "cast", util.cast_attributes + ["character"])
        util.assertListAttrs(self, credits, "crew", util.crew_attributes + ["job"])

    def test_get_tv_episode_groups(self):
        groups = self.tv.episode_groups(self.test3_tv_id)
        util.assertAttrs(self, groups, ["id"])
        self.assertEqual(groups.id, self.test3_tv_id)
        util.assertListAttrs(self, groups, "results", util.episode_group_attributes)

    def test_get_tv_external_ids(self):
        external = self.tv.external_ids(self.test_tv_id)
        util.assertAttrs(self, external, [
            "id", "imdb_id", "tvdb_id", "tvrage_id", "freebase_mid",
            "freebase_id", "facebook_id", "instagram_id", "twitter_id"
        ])
        self.assertEqual(external.id, self.test_tv_id)
        self.assertEqual(external.tvdb_id, 81189)
        self.assertEqual(external.imdb_id, "tt0903747")

    def test_get_tv_images(self):
        images = self.tv.images(self.test_tv_id)
        util.assertAttrs(self, images, ["id"])
        self.assertEqual(images.id, self.test_tv_id)
        util.assertListAttrs(self, images, "backdrops", util.image_attributes + ["iso_639_1"])
        util.assertListAttrs(self, images, "posters", util.image_attributes + ["iso_639_1"])

    def test_get_tv_keywords(self):
        keywords = self.tv.keywords(self.test_tv_id)
        util.assertAttrs(self, keywords, ["id", "results"])
        self.assertEqual(keywords.id, self.test_tv_id)
        util.assertListAttrs(self, keywords, "results", ["id", "name"])

    def test_get_tv_recommendations(self):
        recommendations = self.tv.recommendations(self.test_tv_id)
        util.assertAttrs(self, recommendations, util.pagination_attributes)
        util.assertListAttrs(self, recommendations, "results", util.tv_attributes + ["genre_ids"])

    def test_get_tv_reviews(self):
        reviews = self.tv.reviews(self.test_tv_id)
        util.assertAttrs(self, reviews, util.pagination_attributes)
        util.assertListAttrs(self, reviews, "results", util.review_attributes)

    def test_get_tv_screened_theatrically(self):
        screened_theatrically = self.tv.screened_theatrically(self.test2_tv_id)
        util.assertAttrs(self, screened_theatrically, ["id"])
        self.assertEqual(screened_theatrically.id, self.test2_tv_id)
        util.assertListAttrs(self, screened_theatrically, "results", ["id", "season_number"])

    def test_get_tv_similar(self):
        similar = self.tv.similar(self.test_tv_id)
        util.assertAttrs(self, similar, util.pagination_attributes)
        util.assertListAttrs(self, similar, "results", util.tv_attributes)

    def test_get_tv_translations(self):
        translations = self.tv.translations(self.test_tv_id)
        util.assertAttrs(self, translations, ["id", "translations"])
        self.assertEqual(translations.id, self.test_tv_id)
        util.assertListAttrs(self, translations, "translations", util.translation_attributes)

    def test_get_tv_videos(self):
        videos = self.tv.videos(self.test_tv_id)
        util.assertAttrs(self, videos, ["id", "results"])
        self.assertEqual(videos.id, self.test_tv_id)
        util.assertListAttrs(self, videos, "results", util.video_attributes)

    def test_get_tv_providers(self):
        providers = self.tv.watch_providers(self.test_tv_id)
        util.assertAttrs(self, providers, ["id", "results"])
        self.assertEqual(providers.id, self.test_tv_id)
        self.assertGreater(len(providers.results), 0)

    def test_get_tv_latest(self):
        latest = self.tv.latest()
        util.assertAttrs(self, latest, util.tv_attributes)

    def test_get_tv_airing_today(self):
        airing_today = self.tv.airing_today()
        util.assertAttrs(self, airing_today, util.pagination_attributes)
        util.assertListAttrs(self, airing_today, "results", util.tv_attributes)

    def test_get_tv_on_the_air(self):
        on_the_air = self.tv.on_the_air()
        util.assertAttrs(self, on_the_air, util.pagination_attributes)
        util.assertListAttrs(self, on_the_air, "results", util.tv_attributes)

    def test_get_tv_popular(self):
        popular = self.tv.popular()
        util.assertAttrs(self, popular, util.pagination_attributes)
        util.assertListAttrs(self, popular, "results", util.tv_attributes)

    def test_get_tv_top_rated(self):
        top_rated = self.tv.top_rated()
        util.assertAttrs(self, top_rated, util.pagination_attributes)
        util.assertListAttrs(self, top_rated, "results", util.tv_attributes)
