# -*- coding: utf-8 -*-

import unittest
from tmdbv3api import TMDb


class TMDbTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb('', debug=True)

    def test_get_movie(self):
        movie = self.tmdb.get_movie(111)
        self.assertEqual(movie.title, 'Scarface')
        self.assertEqual(movie.id, 111)
        self.assertTrue(hasattr(movie, 'title'))
        self.assertTrue(hasattr(movie, 'overview'))
        self.assertTrue(hasattr(movie, 'id'))

    def test_get_movie_reviews(self):
        search = self.tmdb.search("Mad Max")
        first = search[0]
        reviews = self.tmdb.get_movie_reviews(first.id)
        self.assertTrue(len(reviews) > 0)
        for review in reviews:
            self.assertTrue(hasattr(review, 'id'))
            self.assertTrue(hasattr(review, 'content'))

    def test_get_movie_lists(self):
        lists = self.tmdb.get_movie_lists(111)
        self.assertTrue(hasattr(lists[0], 'description'))

    def test_get_movie_videos(self):
        videos = self.tmdb.get_movie_videos(111)
        self.assertTrue(hasattr(videos[0], 'id'))

    def test_get_movie_recommendations(self):
        recs = self.tmdb.get_movie_recommendations(111)
        self.assertTrue(hasattr(recs[0], 'id'))

    def test_discover_movies(self):
        discover = self.tmdb.discover_movies({
            'primary_release_year': '2015',
            'with_genres': '28',
            'page': '1',
            'vote_average.gte': '8'

        })
        self.assertTrue(hasattr(discover[0], 'id'))

    def test_discover_tv_shows(self):
        discover = self.tmdb.discover_tv_shows({
            'with_genres': '16',
            'vote_average.gte': '8',
            'page': '1'
        })
        self.assertTrue(hasattr(discover[0], 'id'))

    def test_get_latest_movie(self):
        videos = self.tmdb.get_latest_movie()
        self.assertTrue(hasattr(videos, 'id'))

    def test_now_playing(self):
        now_playing = self.tmdb.now_playing()
        self.assertTrue(hasattr(now_playing[0], 'id'))

    def test_top_rated(self):
        top_rated = self.tmdb.top_rated()
        self.assertTrue(hasattr(top_rated[0], 'id'))

    def test_upcoming(self):
        upcoming = self.tmdb.upcoming()
        self.assertTrue(hasattr(upcoming[0], 'id'))

    def test_popular(self):
        popular = self.tmdb.popular()
        self.assertTrue(hasattr(popular[0], 'id'))

    def test_search(self):
        search = self.tmdb.search('Mad Max')
        self.assertTrue(hasattr(search[0], 'id'))

    def test_similar(self):
        similar = self.tmdb.similar(111)
        self.assertTrue(hasattr(similar[0], 'id'))

    def test_get_tv_show(self):
        show = self.tmdb.get_tv_show(12)
        self.assertTrue(hasattr(show, 'id'))

    def test_get_latest_tv_show(self):
        latest_tv = self.tmdb.get_latest_tv_show()
        self.assertTrue(hasattr(latest_tv, 'id'))

    def test_search_tv(self):
        search_tv = self.tmdb.search_tv('Sunny')
        self.assertTrue(hasattr(search_tv[0], 'id'))

    def test_similar_shows(self):
        similar = self.tmdb.similar(222)
        self.assertTrue(hasattr(similar[0], 'id'))

    def test_popular_shows(self):
        popular = self.tmdb.popular_shows()
        self.assertTrue(hasattr(popular[0], 'id'))

    def test_top_rated_shows(self):
        top_rated = self.tmdb.top_rated_shows()
        self.assertTrue(hasattr(top_rated[0], 'id'))

    def test_get_person(self):
        person = self.tmdb.get_person(234)
        self.assertTrue(hasattr(person, 'id'))

    def test_search_person(self):
        search_person = self.tmdb.search_person('Bryan')
        self.assertTrue(hasattr(search_person[0], 'id'))
