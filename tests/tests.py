# -*- coding: utf-8 -*-

import unittest
import os
import sys
from tmdbv3api import TMDb, Movie, Discover, TV, Person


class TMDbTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb()
        try:
            self.tmdb.api_key = os.environ['api_key']
        except KeyError:
            print("Please set the environment variable for the API key.")
            sys.exit(0)

        self.movie = Movie()
        self.discover = Discover()
        self.tv = TV()
        self.person = Person()

    def test_get_movie(self):
        movie = self.movie.get_movie(111)
        print(movie.title)
        print(movie.id)
        print(movie.overview)
        self.assertIsNotNone(movie)
        self.assertEqual(movie.title, 'Scarface')
        self.assertEqual(movie.id, 111)
        self.assertTrue(hasattr(movie, 'title'))
        self.assertTrue(hasattr(movie, 'overview'))
        self.assertTrue(hasattr(movie, 'id'))

    def test_get_movie_reviews(self):
        search = self.movie.search("Mad Max")
        self.assertTrue(len(search) > 0)
        first = search[0]
        self.assertTrue(first.title == 'Mad Max: Fury Road')
        reviews = self.movie.get_movie_reviews(first.id)
        self.assertTrue(len(reviews) > 0)
        for review in reviews:
            self.assertTrue(hasattr(review, 'id'))
            self.assertTrue(hasattr(review, 'content'))

    def test_get_movie_lists(self):
        lists = self.movie.get_movie_lists(111)
        self.assertTrue(len(lists) > 0)
        self.assertTrue(hasattr(lists[0], 'description'))
        self.assertTrue(hasattr(lists[0], 'name'))

    def test_get_movie_videos(self):
        videos = self.movie.get_movie_videos(111)
        self.assertTrue(len(videos) > 0)
        self.assertTrue(hasattr(videos[0], 'id'))

    def test_get_movie_recommendations(self):
        recs = self.movie.get_movie_recommendations(111)
        for movie in recs:
            print(movie.title)
            print(movie.id)
            print(movie.overview)
        self.assertTrue(len(recs) > 0)
        self.assertTrue(hasattr(recs[0], 'id'))

    def test_discover_movies(self):
        discover = self.discover.discover_movies({
            'primary_release_year': '2015',
            'with_genres': '28',
            'page': '1',
            'vote_average.gte': '8'

        })

        self.assertTrue(len(discover) > 0)
        for movie in discover:
            print(movie.title)
            print(movie.id)
            print(movie.overview)
        self.assertTrue(hasattr(discover[0], 'id'))
        movie = discover[0]

        has_genre = False
        for genre_id in movie.genre_ids:
            if genre_id == 28:
                has_genre = True

        self.assertTrue(movie.vote_average >= 8)
        self.assertTrue(has_genre)

    def test_discover_tv_shows(self):
        discover = self.discover.discover_tv_shows({
            'with_genres': '16',
            'vote_average.gte': '8',
            'page': '1'
        })
        self.assertTrue(len(discover) > 0)
        self.assertTrue(hasattr(discover[0], 'id'))
        movie = discover[0]
        has_genre = False
        for genre_id in movie.genre_ids:
            if genre_id == 16:
                has_genre = True

        self.assertTrue(movie.vote_average >= 8)
        self.assertTrue(has_genre)

    def test_get_latest_movie(self):
        videos = self.movie.get_latest_movie()
        self.assertIsNotNone(videos)
        self.assertTrue(hasattr(videos, 'id'))

    def test_now_playing(self):
        now_playing = self.movie.now_playing()
        self.assertTrue(len(now_playing) > 0)
        for movie in now_playing:
            print(movie.title)
            print(movie.id)
            print(movie.overview)
        self.assertTrue(hasattr(now_playing[0], 'id'))

    def test_top_rated(self):
        top_rated = self.movie.top_rated()
        self.assertTrue(len(top_rated) > 0)
        for movie in top_rated:
            print(movie.title)
            print(movie.id)
            print(movie.overview)
        self.assertTrue(hasattr(top_rated[0], 'id'))

    def test_upcoming(self):
        upcoming = self.movie.upcoming()
        self.assertTrue(len(upcoming) > 0)
        for movie in upcoming:
            print(movie.title)
            print(movie.id)
            print(movie.overview)
        self.assertTrue(hasattr(upcoming[0], 'id'))

    def test_popular(self):
        popular = self.movie.popular()
        self.assertTrue(len(popular) > 0)
        for movie in popular:
            print(movie.title)
            print(movie.id)
            print(movie.overview)
        self.assertTrue(hasattr(popular[0], 'id'))

    def test_search(self):
        search = self.movie.search('Mad Max')
        self.assertTrue(len(search) > 0)
        for movie in search:
            print(movie.title)
            print(movie.id)
            print(movie.overview)
        self.assertTrue(hasattr(search[0], 'id'))

    def test_similar(self):
        similar = self.movie.similar(111)
        self.assertTrue(len(similar) > 0)
        for movie in similar:
            print(movie.title)
            print(movie.id)
            print(movie.overview)
        self.assertTrue(hasattr(similar[0], 'id'))

    def test_get_tv_show(self):
        show = self.tv.get_tv_show(12)
        self.assertIsNotNone(show)
        self.assertTrue(hasattr(show, 'id'))

    def test_get_latest_tv_show(self):
        latest_tv = self.tv.get_latest_tv_show()
        self.assertIsNotNone(latest_tv)
        self.assertTrue(hasattr(latest_tv, 'id'))

    def test_search_tv(self):
        search_tv = self.tv.search_tv('Sunny')
        self.assertTrue(len(search_tv) > 0)
        self.assertTrue(hasattr(search_tv[0], 'id'))

    def test_popular_shows(self):
        popular = self.tv.popular_shows()
        self.assertTrue(len(popular) > 0)
        self.assertTrue(hasattr(popular[0], 'id'))

    def test_top_rated_shows(self):
        top_rated = self.tv.top_rated_shows()
        self.assertTrue(len(top_rated) > 0)
        self.assertTrue(hasattr(top_rated[0], 'id'))

    def test_get_person(self):
        person = self.person.get_by_id(234)
        self.assertIsNotNone(person)
        self.assertTrue(hasattr(person, 'id'))

    def test_search_person(self):
        search_person = self.person.search('Bryan')
        self.assertTrue(len(search_person) > 0)
        self.assertTrue(hasattr(search_person[0], 'id'))
