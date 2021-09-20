# -*- coding: utf-8 -*-

import time
import unittest
import util

from tmdbv3api import Account, Movie, TV, Episode


class CertificationTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = util.setup()
        self.account = Account()
        self.movie = Movie()
        self.tv = TV()
        self.episode = Episode()
        self.test_movie_id = 843906
        self.test_tv_id = 69050
        self.test_season = 5
        self.test_episode = 1
        self.test_rating = 8.5

    def test_get_account_details(self):
        util.assertAttrs(self, self.account.details(), [
            "avatar", "id", "iso_639_1", "iso_3166_1", "include_adult", "username", "name"
        ])

    def test_get_account_created_lists(self):
        lists = self.account.created_lists()
        util.assertAttrs(self, lists, util.pagination_attributes)
        util.assertListAttrs(self, lists, "results", util.list_attributes + ["list_type"])

    def test_get_account_favorite_movies(self):
        self.account.mark_as_favorite(self.test_movie_id, "movie")
        states = self.movie.account_states(self.test_movie_id)
        self.assertTrue(states.favorite)

        movies = self.account.favorite_movies()
        util.assertAttrs(self, movies, util.pagination_attributes)
        util.assertListAttrs(self, movies, "results", util.movie_attributes + ["genre_ids"])

        self.account.unmark_as_favorite(self.test_movie_id, "movie")
        states = self.movie.account_states(self.test_movie_id)
        self.assertFalse(states.favorite)

    def test_get_account_favorite_tv_shows(self):
        self.account.mark_as_favorite(self.test_tv_id, "tv")
        states = self.tv.account_states(self.test_tv_id)
        self.assertTrue(states.favorite)

        shows = self.account.favorite_tv_shows()
        util.assertAttrs(self, shows, util.pagination_attributes)
        util.assertListAttrs(self, shows, "results", util.tv_attributes + ["genre_ids"])

        self.account.unmark_as_favorite(self.test_tv_id, "tv")
        states = self.tv.account_states(self.test_tv_id)
        self.assertFalse(states.favorite)

    def test_get_account_rated_movies(self):
        self.movie.rate_movie(self.test_movie_id, self.test_rating)
        time.sleep(2)
        states = self.movie.account_states(self.test_movie_id)
        self.assertFalse(isinstance(states.rated, bool))
        self.assertEqual(states.rated.value, self.test_rating)

        rated = self.account.rated_movies()
        util.assertAttrs(self, rated, util.pagination_attributes)
        util.assertListAttrs(self, rated, "results", util.movie_attributes + ["rating", "genre_ids"])

        self.movie.delete_rating(self.test_movie_id)
        time.sleep(2)
        states = self.movie.account_states(self.test_movie_id)
        self.assertFalse(states.rated)

    def test_get_account_rated_tv_shows(self):
        self.tv.rate_tv_show(self.test_tv_id, self.test_rating)
        time.sleep(2)
        states = self.tv.account_states(self.test_tv_id)
        self.assertFalse(isinstance(states.rated, bool))
        self.assertEqual(states.rated.value, self.test_rating)

        rated = self.account.rated_tv_shows()
        util.assertAttrs(self, rated, util.pagination_attributes)
        util.assertListAttrs(self, rated, "results", util.tv_attributes + ["rating", "genre_ids"])

        self.tv.delete_rating(self.test_tv_id)
        time.sleep(2)
        states = self.tv.account_states(self.test_tv_id)
        self.assertFalse(states.rated)

    def test_get_account_rated_episodes(self):
        self.episode.rate_tv_episode(self.test_tv_id, self.test_season, self.test_episode, self.test_rating)
        time.sleep(2)
        states = self.episode.account_states(self.test_tv_id, self.test_season, self.test_episode)
        self.assertFalse(isinstance(states.rated, bool))
        self.assertEqual(states.rated.value, self.test_rating)

        rated = self.account.rated_episodes()
        util.assertAttrs(self, rated, util.pagination_attributes)
        util.assertListAttrs(self, rated, "results", util.episode_attributes + ["show_id", "rating"])

        self.episode.delete_rating(self.test_tv_id, self.test_season, self.test_episode)
        time.sleep(2)
        states = self.episode.account_states(self.test_tv_id, self.test_season, self.test_episode)
        self.assertFalse(states.rated)

    def test_get_account_movie_watchlist(self):
        self.account.add_to_watchlist(self.test_movie_id, "movie")
        states = self.movie.account_states(self.test_movie_id)
        self.assertTrue(states.watchlist)

        watchlist = self.account.movie_watchlist()
        util.assertAttrs(self, watchlist, util.pagination_attributes)
        util.assertListAttrs(self, watchlist, "results", util.movie_attributes + ["genre_ids"])

        self.account.remove_from_watchlist(self.test_movie_id, "movie")
        states = self.movie.account_states(self.test_movie_id)
        self.assertFalse(states.watchlist)

    def test_get_account_show_watchlist(self):
        self.account.add_to_watchlist(self.test_tv_id, "tv")
        states = self.tv.account_states(self.test_tv_id)
        self.assertTrue(states.watchlist)

        watchlist = self.account.tv_show_watchlist()
        util.assertAttrs(self, watchlist, util.pagination_attributes)
        util.assertListAttrs(self, watchlist, "results", util.tv_attributes + ["genre_ids"])

        self.account.remove_from_watchlist(self.test_tv_id, "tv")
        states = self.tv.account_states(self.test_tv_id)
        self.assertFalse(states.watchlist)
