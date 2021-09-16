# -*- coding: utf-8 -*-

import os
import unittest

from tmdbv3api import TMDb, Movie


class MovieTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = os.environ["TMDB_API_KEY"]
        self.tmdb.language = "en"
        self.tmdb.debug = True
        self.tmdb.wait_on_rate_limit = True
        self.tmdb.cache = False
        self.movie = Movie()
        self.test_movie_id = 111

    def test_get_movie_repr(self):
        search = self.movie.search("Mad Max")
        self.assertGreater(len(search), 0)
        for result in search:
            self.assertNotEqual(str(result), "TMDB Obj")

    def test_get_movie_details(self):
        movie = self.movie.details(self.test_movie_id)
        self.assertTrue(hasattr(movie, "id"))
        self.assertEqual(movie.id, self.test_movie_id)
        self.assertTrue(hasattr(movie, "title"))
        self.assertTrue(hasattr(movie, "overview"))
        self.assertTrue(hasattr(movie, "release_dates"))

    def test_get_movie_alternative_titles(self):
        alternative_titles = self.movie.alternative_titles(self.test_movie_id)
        self.assertGreater(len(alternative_titles.titles), 0)
        for title in alternative_titles:
            self.assertIn("iso_3166_1", title)
            self.assertIn("title", title)
            self.assertIn("type", title)

    def asset_changes(self, changes):
        self.assertTrue(hasattr(changes, "changes"))
        self.assertGreater(len(changes.changes), 0)
        for change in changes:
            self.assertTrue(hasattr(change, "key"))
            self.assertTrue(hasattr(change, "items"))

    def test_get_movie_changes(self):
        self.asset_changes(self.movie.changes(self.test_movie_id, start_date="2016-08-29", end_date="2016-09-10"))
        self.asset_changes(self.movie.changes(self.test_movie_id, start_date="2016-08-29"))
        self.asset_changes(self.movie.changes(self.test_movie_id, end_date="2016-09-10"))
        self.asset_changes(self.movie.changes(self.test_movie_id, page=2))

    def test_get_movie_credits(self):
        credits = self.movie.credits(self.test_movie_id)
        self.assertTrue(hasattr(credits, "id"))
        self.assertEqual(credits.id, self.test_movie_id)
        self.assertTrue(hasattr(credits, "cast"))
        self.assertTrue(hasattr(credits, "crew"))

    def test_get_movie_external_ids(self):
        external = self.movie.external_ids(self.test_movie_id)
        self.assertTrue(hasattr(external, "id"))
        self.assertEqual(external.id, self.test_movie_id)
        self.assertTrue(hasattr(external, "imdb_id"))
        self.assertEqual(external.imdb_id, "tt0086250")
        self.assertTrue(hasattr(external, "facebook_id"))
        self.assertTrue(hasattr(external, "instagram_id"))
        self.assertTrue(hasattr(external, "twitter_id"))

    def test_get_movie_images(self):
        images = self.movie.images(self.test_movie_id, include_image_language="en,null")
        self.assertTrue(hasattr(images, "id"))
        self.assertEqual(images.id, self.test_movie_id)
        self.assertGreater(len(images.backdrops), 0)
        self.assertGreater(len(images.posters), 0)
        self.assertGreater(len(images.logos), 0)
        for image in images.backdrops:
            self.assertTrue(hasattr(image, "file_path"))
        for image in images.posters:
            self.assertTrue(hasattr(image, "file_path"))
        for image in images.logos:
            self.assertTrue(hasattr(image, "file_path"))

    def test_get_movie_keywords(self):
        keywords = self.movie.keywords(self.test_movie_id)
        self.assertGreater(len(keywords.keywords), 0)
        for keyword in keywords:
            self.assertIn("id", keyword)
            self.assertIn("name", keyword)

    def test_get_movie_lists(self):
        lists = self.movie.lists(self.test_movie_id)
        self.assertTrue(hasattr(lists, "page"))
        self.assertTrue(hasattr(lists, "total_pages"))
        self.assertTrue(hasattr(lists, "total_results"))
        self.assertTrue(hasattr(lists, "results"))
        self.assertGreater(len(lists.results), 0)
        for list in lists:
            self.assertTrue(hasattr(list, "id"))
            self.assertTrue(hasattr(list, "description"))
            self.assertTrue(hasattr(list, "name"))

    def test_get_movie_recommendations(self):
        recommendations = self.movie.recommendations(self.test_movie_id)
        self.assertGreater(len(recommendations), 0)
        for movie in recommendations:
            self.assertTrue(hasattr(movie, "id"))

    def test_get_movie_release_dates(self):
        for release_date in self.movie.release_dates(self.test_movie_id):
            self.assertIn("iso_3166_1", release_date)
            self.assertIn("release_dates", release_date)

    def test_get_movie_reviews(self):
        reviews = self.movie.reviews(self.test_movie_id)
        self.assertGreater(len(reviews), 0)
        for review in reviews:
            self.assertTrue(hasattr(review, "id"))
            self.assertTrue(hasattr(review, "content"))

    def test_get_movie_videos(self):
        videos = self.movie.videos(self.test_movie_id)
        self.assertGreater(len(videos), 0)
        for video in videos:
            self.assertTrue(hasattr(video, "id"))

    def test_get_movie_latest(self):
        latest = self.movie.latest()
        self.assertIsNotNone(latest)
        self.assertTrue(hasattr(latest, "id"))

    def test_get_movie_now_playing(self):
        now_playing = self.movie.now_playing()
        self.assertGreater(len(now_playing), 0)
        for movie in now_playing:
            self.assertTrue(hasattr(movie, "id"))

    def test_get_movie_top_rated(self):
        top_rated = self.movie.top_rated()
        self.assertGreater(len(top_rated), 0)
        for movie in top_rated:
            self.assertTrue(hasattr(movie, "id"))

    def test_get_movie_upcoming(self):
        upcoming = self.movie.upcoming()
        self.assertGreater(len(upcoming), 0)
        for movie in upcoming:
            self.assertTrue(hasattr(movie, "id"))

    def test_get_movie_popular(self):
        popular = self.movie.popular()
        self.assertGreater(len(popular), 0)
        for movie in popular:
            self.assertTrue(hasattr(movie, "id"))

    def test_get_movie_search(self):
        search = self.movie.search("Mad Max")
        self.assertGreater(len(search), 0)
        for movie in search:
            self.assertTrue(hasattr(movie, "id"))

    def test_get_movie_similar(self):
        similar = self.movie.similar(self.test_movie_id)
        self.assertGreater(len(similar), 0)
        for movie in similar:
            self.assertTrue(hasattr(movie, "id"))
    
    def test_get_movie_external(self):
        external = self.movie.external(external_id="tt8155288", external_source="imdb_id")
        self.assertGreater(len(external), 0)
        for movie in external["movie_results"]:
            self.assertIn("id", movie)
            external_ids = self.movie.external_ids(movie["id"])
            self.assertEqual(external_ids["imdb_id"], "tt8155288")