import os

from tmdbv3api import TMDb

movie_attributes = [
    "adult", "backdrop_path", "id", "original_language", "original_title", "overview",
    "release_date", "poster_path", "popularity", "title", "video", "vote_average", "vote_count"
]
tv_attributes = [
    "backdrop_path", "id", "original_language", "original_name", "overview", "first_air_date",
    "poster_path", "popularity", "name", "origin_country", "vote_average", "vote_count"
]
episode_attributes = [
    "air_date", "episode_number", "id", "name", "overview", "production_code",
    "season_number", "still_path", "vote_average", "vote_count"
]
person_attributes = ["id", "name", "gender", "popularity", "profile_path", "adult"]
cast_attributes = ["known_for_department", "order", "original_name"] + person_attributes
crew_attributes = ["known_for_department", "original_name", "department"] + person_attributes
all_person_attributes = [
    "birthday", "deathday", "also_known_as", "biography", "place_of_birth", "imdb_id", "homepage"
] + person_attributes
pagination_attributes = ["page", "total_pages", "total_results", "results"]
image_attributes = ["aspect_ratio", "file_path", "height", "vote_average", "vote_count", "width"]
translation_attributes = ["iso_3166_1", "iso_639_1", "name", "english_name", "data"]
list_attributes = ["description", "favorite_count", "id", "item_count", "iso_639_1", "name", "poster_path"]
alt_titles_attributes = ["iso_3166_1", "title", "type"]
review_attributes = ["author", "author_details", "content", "created_at", "id", "updated_at", "url"]
video_attributes = ["iso_639_1", "iso_3166_1", "name", "key", "published_at", "site", "size", "type", "official", "id"]
episode_group_attributes = ["id", "description", "episode_count", "group_count", "name", "type", "network"]

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
        if list_attribute:
            test.assertTrue(hasattr(items, list_attribute))
            items_list = getattr(items, list_attribute)
        else:
            items_list = items
        test.assertGreater(len(items_list), 0)
    except AssertionError as e:
        e.args = ("(%s) %s" % (list_attribute, e.args[0]),)
        raise
    else:
        for item in items_list:
            assertAttrs(test, item, attributes)