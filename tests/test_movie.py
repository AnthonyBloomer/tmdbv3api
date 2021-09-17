# -*- coding: utf-8 -*-

import unittest
import util

from tmdbv3api import Movie


class MovieTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = util.setup()
        self.movie = Movie()
        self.test_movie_id = 111

    def test_get_movie_details(self):
        details = self.movie.details(self.test_movie_id)
        util.assertAttrs(self, details, util.movie_attributes + ["genres"])
        self.assertEqual(details.id, self.test_movie_id)

    def test_get_movie_alternative_titles(self):
        alternative_titles = self.movie.alternative_titles(self.test_movie_id)
        util.assertListAttrs(self, alternative_titles, "titles", util.alt_titles_attributes)

    def asset_changes(self, changes):
        util.assertAttrs(self, changes, ["changes"])
        util.assertListAttrs(self, changes, "changes", ["key", "items"])

    def test_get_movie_changes(self):
        self.asset_changes(self.movie.changes(self.test_movie_id, start_date="2016-08-29", end_date="2016-09-10"))
        self.asset_changes(self.movie.changes(self.test_movie_id, start_date="2016-08-29"))
        self.asset_changes(self.movie.changes(self.test_movie_id, end_date="2016-09-10"))

    def test_get_movie_credits(self):
        credits = self.movie.credits(self.test_movie_id)
        util.assertAttrs(self, credits, ["id", "cast", "crew"])
        self.assertEqual(credits.id, self.test_movie_id)

    def test_get_movie_external_ids(self):
        external = self.movie.external_ids(self.test_movie_id)
        util.assertAttrs(self, external, ["id", "imdb_id", "facebook_id", "instagram_id", "twitter_id"])
        self.assertEqual(external.id, self.test_movie_id)
        self.assertEqual(external.imdb_id, "tt0086250")

    def test_get_movie_images(self):
        images = self.movie.images(self.test_movie_id, include_image_language="en,null")
        util.assertAttrs(self, images, ["id", "backdrops", "posters", "logos"])
        self.assertEqual(images.id, self.test_movie_id)
        self.assertGreater(len(images.backdrops), 0)
        self.assertGreater(len(images.posters), 0)
        self.assertGreater(len(images.logos), 0)
        for image in images.backdrops:
            util.assertAttrs(self, image, util.image_attributes + ["iso_639_1"])
        for image in images.posters:
            util.assertAttrs(self, image, util.image_attributes + ["iso_639_1"])
        for image in images.logos:
            util.assertAttrs(self, image, util.image_attributes + ["iso_639_1"])

    def test_get_movie_keywords(self):
        keywords = self.movie.keywords(self.test_movie_id)
        util.assertAttrs(self, keywords, ["id", "keywords"])
        self.assertEqual(keywords.id, self.test_movie_id)
        util.assertListAttrs(self, keywords, "keywords", ["id", "name"])

    def test_get_movie_lists(self):
        lists = self.movie.lists(self.test_movie_id)
        util.assertAttrs(self, lists, util.pagination_attributes)
        util.assertListAttrs(self, lists, "results", util.list_attributes + ["list_type"])

    def test_get_movie_recommendations(self):
        recommendations = self.movie.recommendations(self.test_movie_id)
        util.assertAttrs(self, recommendations, util.pagination_attributes)
        util.assertListAttrs(self, recommendations, "results", util.movie_attributes + ["genre_ids"])

    def test_get_movie_release_dates(self):
        release_dates = self.movie.release_dates(self.test_movie_id)
        util.assertAttrs(self, release_dates, ["id", "results"])
        self.assertEqual(release_dates.id, self.test_movie_id)
        util.assertListAttrs(self, release_dates, "results", ["iso_3166_1", "release_dates"])

    def test_get_movie_reviews(self):
        reviews = self.movie.reviews(self.test_movie_id)
        util.assertAttrs(self, reviews, util.pagination_attributes)
        util.assertListAttrs(self, reviews, "results", util.review_attributes)

    def test_get_movie_similar(self):
        similar = self.movie.similar(self.test_movie_id)
        util.assertAttrs(self, similar, util.pagination_attributes)
        util.assertListAttrs(self, similar, "results", util.movie_attributes)

    def test_get_movie_translations(self):
        translations = self.movie.translations(self.test_movie_id)
        util.assertAttrs(self, translations, ["id", "translations"])
        util.assertListAttrs(self, translations, "translations", util.translation_attributes)

    def test_get_movie_videos(self):
        videos = self.movie.videos(self.test_movie_id)
        util.assertAttrs(self, videos, ["id", "results"])
        self.assertEqual(videos.id, self.test_movie_id)
        util.assertListAttrs(self, videos, "results", util.video_attributes)

    def test_get_movie_providers(self):
        providers = self.movie.watch_providers(self.test_movie_id)
        util.assertAttrs(self, providers, ["id", "results"])
        self.assertEqual(providers.id, self.test_movie_id)
        self.assertGreater(len(providers.results), 0)

    def test_get_movie_latest(self):
        latest = self.movie.latest()
        util.assertAttrs(self, latest, util.movie_attributes)

    def test_get_movie_now_playing(self):
        now_playing = self.movie.now_playing()
        util.assertAttrs(self, now_playing, util.pagination_attributes + ["dates"])
        util.assertListAttrs(self, now_playing, "results", util.movie_attributes)

    def test_get_movie_popular(self):
        popular = self.movie.popular()
        util.assertAttrs(self, popular, util.pagination_attributes)
        util.assertListAttrs(self, popular, "results", util.movie_attributes)

    def test_get_movie_top_rated(self):
        top_rated = self.movie.top_rated()
        util.assertAttrs(self, top_rated, util.pagination_attributes)
        util.assertListAttrs(self, top_rated, "results", util.movie_attributes)

    def test_get_movie_upcoming(self):
        upcoming = self.movie.upcoming()
        util.assertAttrs(self, upcoming, util.pagination_attributes)
        util.assertListAttrs(self, upcoming, "results", util.movie_attributes)
