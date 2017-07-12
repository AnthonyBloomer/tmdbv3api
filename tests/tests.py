# -*- coding: utf-8 -*-

import unittest
from tmdbv3api import TMDb


class TMDbTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb('', debug=True)

    def test_get_movie(self):
        movie = self.tmdb.get_movie(111)
        self.assertIsNotNone(movie)
        self.assertEqual(movie.title, 'Scarface')
        self.assertEqual(movie.id, 111)
        self.assertTrue(hasattr(movie, 'title'))
        self.assertTrue(hasattr(movie, 'overview'))
        self.assertTrue(hasattr(movie, 'id'))

    def test_get_movie_reviews(self):
        search = self.tmdb.search("Mad Max")
        self.assertTrue(len(search) > 0)
        first = search[0]
        reviews = self.tmdb.get_movie_reviews(first.id)
        self.assertTrue(len(reviews) > 0)
        for review in reviews:
            self.assertTrue(hasattr(review, 'id'))
            self.assertTrue(hasattr(review, 'content'))

    def test_get_movie_lists(self):
        lists = self.tmdb.get_movie_lists(111)
        self.assertTrue(len(lists) > 0)
        self.assertTrue(hasattr(lists[0], 'description'))

    def test_get_movie_videos(self):
        videos = self.tmdb.get_movie_videos(111)
        self.assertTrue(len(videos) > 0)
        self.assertTrue(hasattr(videos[0], 'id'))

    def test_get_movie_recommendations(self):
        recs = self.tmdb.get_movie_recommendations(111)
        self.assertTrue(len(recs) > 0)
        self.assertTrue(hasattr(recs[0], 'id'))

    def test_discover_movies(self):
        discover = self.tmdb.discover_movies({
            'primary_release_year': '2015',
            'with_genres': '28',
            'page': '1',
            'vote_average.gte': '8'

        })
        self.assertTrue(len(discover) > 0)
        self.assertTrue(hasattr(discover[0], 'id'))
        movie = discover[0]
        for genre_id in movie.genre_ids:
            if genre_id == 28:
                self.assertTrue(True)

        self.assertTrue(movie.vote_average >= 8)

    def test_discover_tv_shows(self):
        discover = self.tmdb.discover_tv_shows({
            'with_genres': '16',
            'vote_average.gte': '8',
            'page': '1'
        })
        self.assertTrue(len(discover) > 0)
        self.assertTrue(hasattr(discover[0], 'id'))
        movie = discover[0]
        for genre_id in movie.genre_ids:
            if genre_id == 16:
                self.assertTrue(True)

        self.assertTrue(movie.vote_average >= 8)

    def test_get_latest_movie(self):
        videos = self.tmdb.get_latest_movie()
        self.assertIsNotNone(videos)
        self.assertTrue(hasattr(videos, 'id'))

    def test_now_playing(self):
        now_playing = self.tmdb.now_playing()
        self.assertTrue(len(now_playing) > 0)
        self.assertTrue(hasattr(now_playing[0], 'id'))

    def test_top_rated(self):
        top_rated = self.tmdb.top_rated()
        self.assertTrue(len(top_rated) > 0)
        self.assertTrue(hasattr(top_rated[0], 'id'))

    def test_upcoming(self):
        upcoming = self.tmdb.upcoming()
        self.assertTrue(len(upcoming) > 0)
        self.assertTrue(hasattr(upcoming[0], 'id'))

    def test_popular(self):
        popular = self.tmdb.popular()
        self.assertTrue(len(popular) > 0)
        self.assertTrue(hasattr(popular[0], 'id'))

    def test_search(self):
        search = self.tmdb.search('Mad Max')
        self.assertTrue(len(search) > 0)
        self.assertTrue(hasattr(search[0], 'id'))

    def test_similar(self):
        similar = self.tmdb.similar(111)
        self.assertTrue(len(similar) > 0)
        self.assertTrue(hasattr(similar[0], 'id'))

    def test_get_tv_show(self):
        show = self.tmdb.get_tv_show(12)
        self.assertIsNotNone(show)
        self.assertTrue(hasattr(show, 'id'))

    def test_get_latest_tv_show(self):
        latest_tv = self.tmdb.get_latest_tv_show()
        self.assertIsNotNone(latest_tv)
        self.assertTrue(hasattr(latest_tv, 'id'))

    def test_search_tv(self):
        search_tv = self.tmdb.search_tv('Sunny')
        self.assertTrue(len(search_tv) > 0)
        self.assertTrue(hasattr(search_tv[0], 'id'))

    def test_similar_shows(self):
        similar = self.tmdb.similar(222)
        self.assertTrue(len(similar) > 0)
        self.assertTrue(hasattr(similar[0], 'id'))

    def test_popular_shows(self):
        popular = self.tmdb.popular_shows()
        self.assertTrue(len(popular) > 0)
        self.assertTrue(hasattr(popular[0], 'id'))

    def test_top_rated_shows(self):
        top_rated = self.tmdb.top_rated_shows()
        self.assertTrue(len(top_rated) > 0)
        self.assertTrue(hasattr(top_rated[0], 'id'))

    def test_get_person(self):
        person = self.tmdb.get_person(234)
        self.assertIsNotNone(person)
        self.assertTrue(hasattr(person, 'id'))

    def test_search_person(self):
        search_person = self.tmdb.search_person('Bryan')
        self.assertTrue(len(search_person) > 0)
        self.assertTrue(hasattr(search_person[0], 'id'))
