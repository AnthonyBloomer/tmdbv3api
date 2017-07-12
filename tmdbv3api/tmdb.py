# -*- coding: utf-8 -*-

import requests
from endpoints import Endpoint
from movie_obj import Movie
from urllib import quote_plus, urlencode


class TMDb:
    def __init__(self, api_key, debug=False, lang='en'):
        self.api_key = api_key
        self.debug = debug
        self.lang = lang

    def get_config(self):
        return self._call(Endpoint.CONFIGURATION, '')

    def get_tv_show(self, show_id, append_to_response="append_to_response=trailers,images,casts,translations"):
        return Movie(**self._call(Endpoint.TV_SHOW % str(show_id), append_to_response))

    def get_latest_tv_show(self):
        return Movie(**self._call(Endpoint.TV_LATEST, ''))

    def search_tv(self, term, page=1):
        return self._get_obj(self._call(Endpoint.SEARCH_TV, 'query=' + quote_plus(term) + '&page=' + str(page)))

    def similar_shows(self, id, page=1):
        return self._get_obj(self._call(Endpoint.TV_SIMILAR % id, 'page=' + str(page)))

    def popular_shows(self, page=1):
        return self._get_obj(self._call(Endpoint.TV_POPULAR, 'page=' + str(page)))

    def top_rated_shows(self, page=1):
        return self._get_obj(self._call(Endpoint.TV_TOP_RATED, 'page=' + str(page)))

    def get_person(self, id):
        return Movie(**self._call(Endpoint.PERSON % str(id), ''))

    def search_person(self, term, page=1):
        return self._get_obj(self._call(Endpoint.SEARCH_PERSON, 'query=' + quote_plus(term) + '&page=' + str(page)))

    def discover_movies(self, params):
        return self._get_obj(self._call(Endpoint.DISCOVER_MOVIES, urlencode(params)))

    def discover_tv_shows(self, params):
        return self._get_obj(self._call(Endpoint.DISCOVER_TV, urlencode(params)))

    def get_movie(self, movie_id, append_to_response="append_to_response=trailers,images,casts,translations"):
        return Movie(**self._call(Endpoint.MOVIE + str(movie_id), append_to_response))

    def get_movie_reviews(self, id, page=1):
        return self._get_obj(self._call(Endpoint.MOVIE_REVIEWS % id, 'page=' + str(page)))

    def get_movie_lists(self, id, page=1):
        return self._get_obj(self._call(Endpoint.MOVIE_LISTS % id, 'page=' + str(page)))

    def get_movie_videos(self, id, page=1):
        return self._get_obj(self._call(Endpoint.MOVIE_VIDEOS % id, 'page=' + str(page)))

    def get_movie_recommendations(self, movie_id, page=1):
        return self._get_obj(self._call(Endpoint.MOVIE_RECOMMENDATIONS % movie_id, 'page=' + str(page)))

    def get_latest_movie(self):
        return Movie(**self._call(Endpoint.MOVIE_LATEST, ''))

    def now_playing(self, page=1):
        return self._get_obj(self._call(Endpoint.NOW_PLAYING, 'page=' + str(page)))

    def top_rated(self, page=1):
        return self._get_obj(self._call(Endpoint.TOP_RATED, 'page=' + str(page)))

    def upcoming(self, page=1):
        return self._get_obj(self._call(Endpoint.UPCOMING, 'page=' + str(page)))

    def popular(self, page=1):
        return self._get_obj(self._call(Endpoint.POPULAR, 'page=' + str(page)))

    def search(self, term, page=1):
        return self._get_obj(self._call(Endpoint.SEARCH_MOVIE, "query=" + quote_plus(term) + "&page=" + str(page)))

    def similar(self, id, page=1):
        return self._get_obj(self._call(Endpoint.MOVIE_SIMILAR % id, 'page=' + str(page)))

    def _get_obj(self, result):
        arr = []
        [arr.append(Movie(**res)) for res in result['results']]
        return arr

    def _call(self, action, append_to_response):
        url = "%s%s?api_key=%s&%s&language=%s" % (Endpoint.BASE, action, self.api_key, append_to_response, self.lang)

        req = requests.get(url)

        if req.status_code != 200:
            req.raise_for_status()

        json = req.json()

        if 'errors' in json:
            raise Exception(json['errors'])

        return json
