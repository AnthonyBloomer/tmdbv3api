# -*- coding: utf-8 -*-

import os
import time
import unittest
import assert_helper

from tmdbv3api import TMDb, Account, Movie, TV, Episode


class CertificationTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = assert_helper.setup()
        self.account = Account()
        self.movie = Movie()
        self.tv = TV()
        self.episode = Episode()
        self.test_movie_id = 843906
        self.test_show_id = 69050
        self.test_season = 5
        self.test_episode = 1
        self.test_rating = 8.5

    def test_get_account_details(self):
        details = self.account.details()
        self.assertIn("avatar", details)
        self.assertIn("id", details)
        self.assertIn("iso_639_1", details)
        self.assertIn("iso_3166_1", details)
        self.assertIn("name", details)
        self.assertIn("include_adult", details)
        self.assertIn("username", details)

    def test_get_account_created_lists(self):
        lists = self.account.created_lists()
        self.assertGreater(len(lists.results), 0)
        self.assertTrue(hasattr(lists, "page"))
        self.assertTrue(hasattr(lists, "total_pages"))
        self.assertTrue(hasattr(lists, "total_results"))
        self.assertIn("description", lists[0])
        self.assertIn("favorite_count", lists[0])
        self.assertIn("id", lists[0])
        self.assertIn("item_count", lists[0])
        self.assertIn("iso_639_1", lists[0])
        self.assertIn("list_type", lists[0])
        self.assertIn("name", lists[0])
        self.assertIn("poster_path", lists[0])

    def assert_movies(self, movies):
        assert_helper.assert_pagination(self, movies)
        self.assertIn("adult", movies[0])
        self.assertIn("backdrop_path", movies[0])
        self.assertIn("genre_ids", movies[0])
        self.assertIn("id", movies[0])
        self.assertIn("original_language", movies[0])
        self.assertIn("original_title", movies[0])
        self.assertIn("overview", movies[0])
        self.assertIn("release_date", movies[0])
        self.assertIn("poster_path", movies[0])
        self.assertIn("popularity", movies[0])
        self.assertIn("title", movies[0])
        self.assertIn("video", movies[0])
        self.assertIn("vote_average", movies[0])
        self.assertIn("vote_count", movies[0])

    def assert_tv_shows(self, shows):
        assert_helper.assert_pagination(self, shows)
        self.assertIn("backdrop_path", shows[0])
        self.assertIn("genre_ids", shows[0])
        self.assertIn("id", shows[0])
        self.assertIn("original_language", shows[0])
        self.assertIn("original_name", shows[0])
        self.assertIn("overview", shows[0])
        self.assertIn("first_air_date", shows[0])
        self.assertIn("poster_path", shows[0])
        self.assertIn("popularity", shows[0])
        self.assertIn("name", shows[0])
        self.assertIn("origin_country", shows[0])
        self.assertIn("vote_average", shows[0])
        self.assertIn("vote_count", shows[0])

    def test_get_account_favorite_movies(self):
        self.account.mark_as_favorite(self.test_movie_id, "movie")
        states = self.movie.account_states(self.test_movie_id)
        self.assertTrue(states.favorite)

        self.assert_movies(self.account.favorite_movies())

        self.account.unmark_as_favorite(self.test_movie_id, "movie")
        states = self.movie.account_states(self.test_movie_id)
        self.assertFalse(states.favorite)

    def test_get_account_favorite_tv_shows(self):
        self.account.mark_as_favorite(self.test_show_id, "tv")
        states = self.tv.account_states(self.test_show_id)
        self.assertTrue(states.favorite)

        self.assert_tv_shows(self.account.favorite_tv_shows())

        self.account.unmark_as_favorite(self.test_show_id, "tv")
        states = self.tv.account_states(self.test_show_id)
        self.assertFalse(states.favorite)

    def test_get_account_rated_movies(self):
        self.movie.rate_movie(self.test_movie_id, self.test_rating)
        time.sleep(2)
        states = self.movie.account_states(self.test_movie_id)
        self.assertFalse(isinstance(states.rated, bool))
        self.assertEqual(states.rated.value, self.test_rating)

        self.assert_movies(self.account.rated_movies())

        self.movie.delete_rating(self.test_movie_id)
        time.sleep(2)
        states = self.movie.account_states(self.test_movie_id)
        self.assertFalse(states.rated)

    def test_get_account_rated_tv_shows(self):
        self.tv.rate_tv_show(self.test_show_id, self.test_rating)
        time.sleep(2)
        states = self.tv.account_states(self.test_show_id)
        self.assertFalse(isinstance(states.rated, bool))
        self.assertEqual(states.rated.value, self.test_rating)

        self.assert_tv_shows(self.account.rated_tv_shows())

        self.tv.delete_rating(self.test_show_id)
        time.sleep(2)
        states = self.tv.account_states(self.test_show_id)
        self.assertFalse(states.rated)

    def test_get_account_rated_episodes(self):
        self.episode.rate_tv_episode(self.test_show_id, self.test_season, self.test_episode, self.test_rating)
        time.sleep(2)
        states = self.episode.account_states(self.test_show_id, self.test_season, self.test_episode)
        self.assertFalse(isinstance(states.rated, bool))
        self.assertEqual(states.rated.value, self.test_rating)

        episodes = self.account.rated_episodes()
        assert_helper.assert_pagination(self, episodes)
        self.assertIn("air_date", episodes[0])
        self.assertIn("episode_number", episodes[0])
        self.assertIn("id", episodes[0])
        self.assertIn("name", episodes[0])
        self.assertIn("overview", episodes[0])
        self.assertIn("production_code", episodes[0])
        self.assertIn("season_number", episodes[0])
        self.assertIn("show_id", episodes[0])
        self.assertIn("still_path", episodes[0])
        self.assertIn("vote_average", episodes[0])
        self.assertIn("vote_count", episodes[0])
        self.assertIn("rating", episodes[0])

        self.episode.delete_rating(self.test_show_id, self.test_season, self.test_episode)
        time.sleep(2)
        states = self.episode.account_states(self.test_show_id, self.test_season, self.test_episode)
        self.assertFalse(states.rated)

    def test_get_account_movie_watchlist(self):
        self.account.add_to_watchlist(self.test_movie_id, "movie")
        states = self.movie.account_states(self.test_movie_id)
        self.assertTrue(states.watchlist)

        self.assert_movies(self.account.movie_watchlist())

        self.account.remove_from_watchlist(self.test_movie_id, "movie")
        states = self.movie.account_states(self.test_movie_id)
        self.assertFalse(states.watchlist)

    def test_get_account_show_watchlist(self):
        self.account.add_to_watchlist(self.test_show_id, "tv")
        states = self.tv.account_states(self.test_show_id)
        self.assertTrue(states.watchlist)

        self.assert_tv_shows(self.account.tv_show_watchlist())

        self.account.remove_from_watchlist(self.test_show_id, "tv")
        states = self.tv.account_states(self.test_show_id)
        self.assertFalse(states.watchlist)
