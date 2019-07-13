# -*- coding: utf-8 -*-

import unittest
import os
from tmdbv3api import TMDb, Movie, Discover, TV, Person, Collection, Company, Configuration, Genre, Season


class TMDbTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = 'e1076b74406e0a7d0efb5318f1b662d0'
        self.tmdb.language = 'en'
        self.tmdb.debug = True
        self.tmdb.wait_on_rate_limit = True
        self.movie = Movie()
        self.discover = Discover()
        self.tv = TV()
        self.person = Person()
        self.collection = Collection()
        self.company = Company()
        self.season = Season()

    def test_get_movie_repr(self):
        search = self.movie.search("Mad Max")
        for results in search:
            print(results)

    def test_get_tv_show_repr(self):
        search_tv = self.tv.search('Sunny')
        for results in search_tv:
            print(results)

    def test_get_movie(self):
        movie = self.movie.details(111)
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
        reviews = self.movie.reviews(first.id)
        self.assertTrue(len(reviews) > 0)
        for review in reviews:
            self.assertTrue(hasattr(review, 'id'))
            self.assertTrue(hasattr(review, 'content'))

    def test_get_movie_lists(self):
        lists = self.movie.lists(111)
        self.assertTrue(len(lists) > 0)
        self.assertTrue(hasattr(lists[0], 'description'))
        self.assertTrue(hasattr(lists[0], 'name'))

    def test_get_movie_videos(self):
        videos = self.movie.videos(111)
        self.assertTrue(len(videos) > 0)
        self.assertTrue(hasattr(videos[0], 'id'))

    def test_get_movie_recommendations(self):
        recs = self.movie.recommendations(111)
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
        self.assertTrue(hasattr(discover[0], 'id'))
        movie = discover[0]

        has_genre = False
        for genre_id in movie.genre_ids:
            if genre_id == 28:
                has_genre = True
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
        self.assertTrue(has_genre)

    def test_get_latest_movie(self):
        videos = self.movie.latest()
        self.assertIsNotNone(videos)
        self.assertTrue(hasattr(videos, 'id'))

    def test_now_playing(self):
        now_playing = self.movie.now_playing()
        self.assertTrue(len(now_playing) > 0)
        self.assertTrue(hasattr(now_playing[0], 'id'))

    def test_top_rated(self):
        top_rated = self.movie.top_rated()
        self.assertTrue(len(top_rated) > 0)
        self.assertTrue(hasattr(top_rated[0], 'id'))

    def test_upcoming(self):
        upcoming = self.movie.upcoming()
        self.assertTrue(len(upcoming) > 0)
        self.assertTrue(hasattr(upcoming[0], 'id'))

    def test_popular(self):
        popular = self.movie.popular()
        self.assertTrue(len(popular) > 0)
        self.assertTrue(hasattr(popular[0], 'id'))

    def test_search(self):
        search = self.movie.search('Mad Max')
        self.assertTrue(len(search) > 0)
        self.assertTrue(hasattr(search[0], 'id'))

    def test_similar(self):
        similar = self.movie.similar(111)
        self.assertTrue(len(similar) > 0)
        self.assertTrue(hasattr(similar[0], 'id'))

    def test_get_tv_show(self):
        show = self.tv.details(12)
        self.assertIsNotNone(show)
        self.assertTrue(hasattr(show, 'id'))

    def test_get_latest_tv_show(self):
        latest_tv = self.tv.latest()
        self.assertIsNotNone(latest_tv)
        self.assertTrue(hasattr(latest_tv, 'id'))

    def test_search_tv(self):
        search_tv = self.tv.search('Sunny')
        self.assertTrue(len(search_tv) > 0)
        self.assertTrue(hasattr(search_tv[0], 'id'))

    def test_popular_shows(self):
        popular = self.tv.popular()
        self.assertTrue(len(popular) > 0)
        self.assertTrue(hasattr(popular[0], 'id'))

    def test_top_rated_shows(self):
        top_rated = self.tv.top_rated()
        self.assertTrue(len(top_rated) > 0)
        self.assertTrue(hasattr(top_rated[0], 'id'))

    def test_get_person(self):
        person = self.person.details(234)
        self.assertIsNotNone(person)
        self.assertTrue(hasattr(person, 'id'))

    def test_search_person(self):
        search_person = self.person.search('Bryan')
        self.assertTrue(len(search_person) > 0)
        self.assertTrue(hasattr(search_person[0], 'id'))

    def test_collection_details(self):
        c = Collection()
        details = c.details(10)
        self.assertEqual(details.name, 'Star Wars Collection')
        self.assertEqual(details.id, 10)
        self.assertTrue(hasattr(details, 'overview'))
        self.assertTrue(hasattr(details, 'poster_path'))

    def test_collection_images(self):
        c = Collection()
        images = c.images(10)
        self.assertTrue(hasattr(images, 'backdrops'))
        self.assertTrue(hasattr(images, 'posters'))

    def test_popular_people(self):
        popular = self.person.popular()
        self.assertTrue(len(popular) > 0)
        first = popular[0]
        self.assertTrue(hasattr(first, 'name'))
        self.assertTrue(hasattr(first, 'known_for'))

    def test_latest_person(self):
        latest_person = self.person.latest()
        self.assertIsNotNone(latest_person)
        self.assertTrue(hasattr(latest_person, 'name'))
        self.assertTrue(hasattr(latest_person, 'id'))

    def test_person_images(self):
        images = self.person.images(11)
        self.assertIsNotNone(images)
        self.assertTrue(hasattr(images, 'profiles'))
        self.assertTrue(hasattr(images, 'id'))

    def test_company_details(self):
        c = self.company.details(1)
        self.assertTrue(hasattr(c, 'name'))
        self.assertEqual(c.name, 'Lucasfilm')

    def test_company_movies(self):
        company = self.company.movies(1)
        self.assertTrue(len(company) > 0)
        first = company[0]
        self.assertTrue(hasattr(first, 'title'))
        self.assertTrue(hasattr(first, 'overview'))

    def test_config(self):
        config = Configuration()
        info = config.info()
        self.assertIsNotNone(info)
        self.assertTrue(hasattr(info, 'images'))

    def test_genres(self):
        genres = Genre()
        movie_genres = genres.movie_list()
        self.assertIsNotNone(movie_genres)
        tv_genres = genres.tv_list()
        self.assertIsNotNone(tv_genres)

    def test_season(self):
        s = self.season.details(1418, 1)
        self.assertIsNotNone(s)
        self.assertEqual(s.name, 'Season 1')
        self.assertEqual(s.id, 3738)
        self.assertTrue(hasattr(s, 'episodes'))
        self.assertTrue(hasattr(s, 'overview'))
        self.assertTrue(hasattr(s, 'id'))

    def test_get_season_changes(self):
        s = self.season.changes(1418, 1)
        self.assertIsNotNone(s)

    def test_get_season_external_ids(self):
        s = self.season.external_ids(1418, 1)
        self.assertIsNotNone(s)
        self.assertIsNotNone(s['tvdb_id'])

    def test_get_season_videos(self):
        s = self.season.videos(1418, 1)

    def test_get_season_images(self):
        s = self.season.images(1418, 1)
        for l in s:
            self.assertIsNotNone(l.width)
            self.assertIsNotNone(l.height)

    def test_get_season_credits(self):
        s = self.season.credits(1418, 1)
        for c in s:
            self.assertIsNotNone(c.name)
            self.assertIsNotNone(c.character)

    def test_get_movie_by_external_id(self):
        ex = self.movie.external(external_id="tt8155288", external_source="imdb_id")
        res = ex['movie_results'][0]
        self.assertTrue(res['title'] == "Happy Death Day 2U")
