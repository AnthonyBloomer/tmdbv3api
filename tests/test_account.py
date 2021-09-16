# -*- coding: utf-8 -*-

import os
import time
import unittest

from tmdbv3api import TMDb, Account, Movie, TV, Episode


class CertificationTests(unittest.TestCase):
    def setUp(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = os.environ["TMDB_API_KEY"]
        self.tmdb.language = "en-US"
        self.tmdb.debug = True
        self.tmdb.wait_on_rate_limit = True
        self.tmdb.cache = False
        self.account = Account()
        self.movie = Movie()
        self.tv = TV()
        self.episode = Episode()

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
        self.assertTrue(hasattr(movies, "page"))
        self.assertTrue(hasattr(movies, "total_pages"))
        self.assertTrue(hasattr(movies, "total_results"))
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
        self.assertTrue(hasattr(shows, "page"))
        self.assertTrue(hasattr(shows, "total_pages"))
        self.assertTrue(hasattr(shows, "total_results"))
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
        self.account.mark_as_favorite(843906, "movie")
        states = self.movie.account_states(843906)
        self.assertTrue(states.favorite)

        self.assert_movies(self.account.favorite_movies())

        self.account.unmark_as_favorite(843906, "movie")
        states = self.movie.account_states(843906)
        self.assertFalse(states.favorite)

    def test_get_account_favorite_tv_shows(self):
        self.account.mark_as_favorite(69050, "tv")
        states = self.tv.account_states(69050)
        self.assertTrue(states.favorite)

        self.assert_tv_shows(self.account.favorite_tv_shows())

        self.account.unmark_as_favorite(69050, "tv")
        states = self.tv.account_states(69050)
        self.assertFalse(states.favorite)

    def test_get_account_rated_movies(self):
        self.movie.rate_movie(843906, 8.5)
        time.sleep(2)
        states = self.movie.account_states(843906)
        self.assertFalse(isinstance(states.rated, bool))
        self.assertEqual(states.rated.value, 8.5)

        self.assert_movies(self.account.rated_movies())

        self.movie.delete_rating(843906)
        time.sleep(2)
        states = self.movie.account_states(843906)
        self.assertFalse(states.rated)

    def test_get_account_rated_tv_shows(self):
        self.tv.rate_tv_show(69050, 8.5)
        time.sleep(2)
        states = self.tv.account_states(69050)
        self.assertFalse(isinstance(states.rated, bool))
        self.assertEqual(states.rated.value, 8.5)

        self.assert_tv_shows(self.account.rated_tv_shows())

        self.tv.delete_rating(69050)
        time.sleep(2)
        states = self.tv.account_states(69050)
        self.assertFalse(states.rated)

    def test_get_account_rated_episodes(self):
        self.episode.rate_tv_episode(69050, 5, 1, 8.5)
        time.sleep(2)
        states = self.episode.account_states(69050, 5, 1)
        self.assertFalse(isinstance(states.rated, bool))
        self.assertEqual(states.rated.value, 8.5)

        episodes = self.account.rated_episodes()
        self.assertTrue(hasattr(episodes, "page"))
        self.assertTrue(hasattr(episodes, "total_pages"))
        self.assertTrue(hasattr(episodes, "total_results"))
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

        self.episode.delete_rating(69050, 5, 1)
        time.sleep(2)
        states = self.episode.account_states(69050, 5, 1)
        self.assertFalse(states.rated)

    def test_get_account_movie_watchlist(self):
        self.account.add_to_watchlist(843906, "movie")
        states = self.movie.account_states(843906)
        self.assertTrue(states.watchlist)

        self.assert_movies(self.account.movie_watchlist())

        self.account.remove_from_watchlist(843906, "movie")
        states = self.movie.account_states(843906)
        self.assertFalse(states.watchlist)

    def test_get_account_show_watchlist(self):
        self.account.add_to_watchlist(69050, "tv")
        states = self.tv.account_states(69050)
        self.assertTrue(states.watchlist)

        self.assert_tv_shows(self.account.tv_show_watchlist())

        self.account.remove_from_watchlist(69050, "tv")
        states = self.tv.account_states(69050)
        self.assertFalse(states.watchlist)







