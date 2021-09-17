import os

from tmdbv3api import TMDb

movie_attributes = [
    "adult", "backdrop_path", "id", "original_language", "original_title", "overview",
    "release_date", "poster_path", "popularity", "title", "video", "vote_average", "vote_count"
]
show_attributes = [
    "backdrop_path", "genre_ids", "id", "original_language", "original_name", "overview", "first_air_date",
    "poster_path", "popularity", "name", "origin_country", "vote_average", "vote_count"
]
episode_attributes = [
    "air_date", "episode_number", "id", "name", "overview", "production_code",
    "season_number", "still_path", "vote_average", "vote_count"
]
pagination_attributes = ["page", "total_pages", "total_results", "results"]
image_attributes = ["aspect_ratio", "file_path", "height", "vote_average", "vote_count", "width"]
translation_attributes = ["iso_3166_1", "iso_639_1", "name", "english_name", "data"]
list_attributes = ["description", "favorite_count", "id", "item_count", "iso_639_1", "name", "poster_path"]
alt_titles_attributes = ["iso_3166_1", "title", "type"]
review_attributes = ["author", "author_details", "content", "created_at", "id", "updated_at", "url"]
video_attributes = ["iso_639_1", "iso_3166_1", "name", "key", "published_at", "site", "size", "type", "official", "id"]


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
        try:
            test.assertTrue(hasattr(items, attribute))
        except AssertionError as e:
            e.args = ("(%s) %s" % (attribute, e.args[0]),)
            raise


def assertListAttrs(test, items, list_attribute, attributes):
    try:
        test.assertTrue(hasattr(items, list_attribute))
        test.assertGreater(len(getattr(items, list_attribute)), 0)
    except AssertionError as e:
        e.args = ("(%s) %s" % (list_attribute, e.args[0]),)
        raise
    for item in items:
        assertAttrs(test, item, attributes)

def test_get_movie_search(self):
    search = self.movie.search("Mad Max")
    self.assertGreater(len(search), 0)
    for movie in search:
        self.assertTrue(hasattr(movie, "id"))

def test_get_movie_external(self):
    external = self.movie.external(external_id="tt8155288", external_source="imdb_id")
    self.assertGreater(len(external), 0)
    for movie in external["movie_results"]:
        self.assertIn("id", movie)
        external_ids = self.movie.external_ids(movie["id"])
        self.assertEqual(external_ids["imdb_id"], "tt8155288")

def test_get_movie_repr(self):
    search = self.movie.search("Mad Max")
    self.assertGreater(len(search), 0)
    for result in search:
        self.assertNotEqual(str(result), "TMDB Obj")