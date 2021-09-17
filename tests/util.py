import os

from tmdbv3api import TMDb

movie_attributes = [
    "adult", "backdrop_path", "genre_ids", "id", "original_language", "original_title", "overview",
    "release_date", "poster_path", "popularity", "title", "video", "vote_average", "vote_count"
]
show_attributes = [
    "backdrop_path", "genre_ids", "id", "original_language", "original_name", "overview", "first_air_date",
    "poster_path", "popularity", "name", "origin_country", "vote_average", "vote_count"
]
episode_attributes = [
    "air_date", "episode_number", "id", "name", "overview", "production_code", "season_number",
    "show_id", "still_path", "vote_average", "vote_count"
]
pagination_attributes = ["page", "total_pages", "total_results", "results"]
image_attributes = ["aspect_ratio", "file_path", "height", "iso_639_1", "vote_average", "vote_count", "width"]
translation_attributes = ["iso_3166_1", "iso_639_1", "name", "english_name", "data"]
list_attributes = ["description", "favorite_count", "id", "item_count", "iso_639_1", "name", "poster_path"]

def setup():
    tmdb = TMDb()
    tmdb.api_key = os.environ["TMDB_API_KEY"]
    tmdb.language = "en"
    tmdb.debug = True
    tmdb.wait_on_rate_limit = True
    tmdb.cache = False
    return tmdb

def assertAttrs(test, items, attributes):
    for attribute in attributes:
        test.assertTrue(hasattr(items, attribute))

def assertListAttrs(test, items, list_attribute, attributes):
    test.assertTrue(hasattr(items, list_attribute))
    test.assertGreater(len(getattr(items, list_attribute)), 0)
    for item in items:
        assertAttrs(test, item, attributes)
