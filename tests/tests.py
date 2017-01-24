# -*- coding: utf-8 -*-

import unittest
from tmdbv3api import TMDb
import pprint


class TMDbTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb('', debug=True)

    def test_get_movie(self):
        movie = self.tmdb.get_movie(111)
        self.assertEqual(movie.title, 'Scarface')

    def test_get_movie_reviews(self):
        movie = self.tmdb.get_movie_reviews(12)
        self.assertTrue(movie)

    def test_get_movie_lists(self):
        lists = self.tmdb.get_movie_lists(111)
        self.assertTrue(hasattr(lists[0], 'description'))

    def test_get_movie_videos(self):
        videos = self.tmdb.get_movie_videos(111)
        self.assertTrue(hasattr(videos[0], 'id'))

    def test_get_movie_recommendations(self):
        pass

    def test_discover_movies(self):
        pass

    def test_discover_tv_shows(self):
        pass

    def test_get_latest_movie(self):
        pass

    def test_now_playing(self):
        pass

    def test_top_rated(self):
        pass

    def test_upcoming(self):
        pass

    def test_popular(self):
        pass

    def test_search(self):
        pass

    def test_similar(self):
        pass

    def test_get_tv_show(self):
        pass

    def test_get_latest_tv_show(self):
        pass

    def test_search_tv(self):
        pass

    def test_similar_shows(self):
        pass

    def test_popular_shows(self):
        pass

    def test_top_rated_shows(self):
        pass

    def test_get_person(self):
        pass

    def test_search_person(self):
        pass
