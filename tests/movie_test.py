# -*- coding: utf-8 -*-

import os
import unittest

from tmdbv3api import TMDb, Movie


class MovieTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = os.environ['TMDB_API_KEY']
        self.tmdb.language = "en"
        self.tmdb.debug = True
        self.tmdb.wait_on_rate_limit = True
        self.tmdb.cache = False
        self.movie = Movie()

    def test_get_movie_repr(self):
        search = self.movie.search("Mad Max")
        self.assertGreater(len(search), 0)
        for result in search:
            self.assertNotEqual(str(result), "TMDB Obj")

    def test_get_movie_details(self):
        movie = self.movie.details(111)
        self.assertIsNotNone(movie)
        self.assertEqual(movie.id, 111)
        self.assertTrue(hasattr(movie, 'title'))
        self.assertTrue(hasattr(movie, 'overview'))
        self.assertTrue(hasattr(movie, 'release_dates'))

    def test_get_movie_alternative_titles(self):
        alternative_titles = self.movie.alternative_titles(111)
        self.assertEqual(alternative_titles.id, 111)
        self.assertGreater(len(alternative_titles.titles), 0)
        for title in alternative_titles.titles:
            self.assertIn('iso_3166_1', title)
            self.assertIn('title', title)
            self.assertIn('type', title)

    def test_get_movie_changes(self):
        changes = self.movie.changes(111, start_date="2016-08-29", end_date="2016-09-10")
        self.assertIsNotNone(changes)
        changes = self.movie.changes(111, start_date="2016-08-29")
        self.assertIsNotNone(changes)
        changes = self.movie.changes(111, end_date="2016-09-10")
        self.assertIsNotNone(changes)
        changes = self.movie.changes(111, page=2)
        self.assertIsNotNone(changes)

    def test_get_movie_credits(self):
        credits = self.movie.credits(111)
        self.assertEqual(credits.id, 111)
        self.assertTrue(hasattr(credits, "cast"))
        self.assertTrue(hasattr(credits, "crew"))

    def test_get_movie_external_ids(self):
        external_ids = self.movie.external_ids(111)
        self.assertIn("imdb_id", external_ids)
        self.assertIn("facebook_id", external_ids)
        self.assertIn("instagram_id", external_ids)
        self.assertIn("twitter_id", external_ids)
        self.assertIn("id", external_ids)

    def test_get_movie_images(self):
        images = self.movie.images(111, include_image_language="en,null")
        self.assertEqual(images.id, 111)
        self.assertGreater(len(images.backdrops), 0)
        self.assertGreater(len(images.posters), 0)
        for image in images.backdrops:
            self.assertIn("file_path", image)
        for image in images.posters:
            self.assertIn("file_path", image)

    def test_get_movie_keywords(self):
        keywords = self.movie.keywords(111)
        for keyword in keywords.keywords:
            self.assertIn("id", keyword)
            self.assertIn("name", keyword)

    def test_get_movie_lists(self):
        lists = self.movie.lists(111)
        self.assertGreater(len(lists), 0)
        for list in lists:
            self.assertTrue(hasattr(list, "description"))
            self.assertTrue(hasattr(list, "name"))

    def test_get_movie_recommendations(self):
        recommendations = self.movie.recommendations(111)
        self.assertGreater(len(recommendations), 0)
        for movie in recommendations:
            self.assertTrue(hasattr(movie, "id"))

    def test_get_movie_release_dates(self):
        release_dates = self.movie.release_dates(111)
        self.assertIsNotNone(release_dates)
        self.assertEqual(release_dates.id, 111)

    def test_get_movie_reviews(self):
        reviews = self.movie.reviews(111)
        self.assertGreater(len(reviews), 0)
        for review in reviews:
            self.assertTrue(hasattr(review, "id"))
            self.assertTrue(hasattr(review, "content"))

    def test_get_movie_videos(self):
        videos = self.movie.videos(111)
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
        similar = self.movie.similar(111)
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

    def test_get_watch_providers(self):
        watch_providers = self.movie.watch_providers(111)
        self.assertTrue(hasattr(watch_providers, "id"))
        self.assertTrue(hasattr(watch_providers, 'results'))
