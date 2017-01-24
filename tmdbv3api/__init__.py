# -*- coding: utf-8 -*-

import json
import pprint
from urllib import quote_plus, urlopen, urlencode


class obj:
    def __init__(self, **entries):
        self.__dict__.update(entries)


# http://docs.themoviedb.apiary.io
class TMDb:
    URL = "http://api.themoviedb.org/3/"

    def __init__(self, api_key, debug=False, lang='en'):
        self.api_key = api_key
        self.debug = debug
        self.lang = lang

    def get_config(self):
        return self._call('configuration', '')

    # Get the basic movie information for a specific movie id.
    def get_movie(self, movie_id, append_to_response="append_to_response=trailers,images,casts,translations"):
        return obj(**self._call('movie/' + str(movie_id), append_to_response))

    # Get the user reviews for a movie
    def get_movie_reviews(self, id, page=1):
        arr = []
        result = self._call('movie/%s/reviews' % id, 'page=' + str(page))
        if result['total_results'] > 0:
            [arr.append(obj(**res)) for res in result['results']]
        return arr

    def get_movie_lists(self, id, page=1):
        arr = []
        result = self._call('movie/%s/lists' % id, 'page=' + str(page))
        [arr.append(obj(**res)) for res in result['results']]
        return arr

    def get_movie_videos(self, id, page=1):
        arr = []
        result = self._call('movie/%s/videos' % id, 'page=' + str(page))
        [arr.append(obj(**res)) for res in result['results']]
        return arr

    def get_movie_recommendations(self, movie_id, page=1):
        arr = []
        result = self._call('movie/%s/recommendations' % movie_id, 'page=' + str(page))
        [arr.append(obj(**res)) for res in result['results']]
        return arr

    def discover_movies(self, params):
        arr = []
        result = self._call('discover/movie/', urlencode(params))
        [arr.append(obj(**res)) for res in result['results']]
        return arr

    def discover_tv_shows(self, params):
        arr = []
        result = self._call('discover/tv/', urlencode(params))
        [arr.append(obj(**res)) for res in result['results']]
        return arr

    # Get the latest movie id.
    def get_latest_movie(self):
        return obj(**self._call('movie/latest', ''))

    # Get the list of movies playing that have been, or are being released this week. This list refreshes every day.
    def now_playing(self, page=1):
        arr = []
        result = self._call('movie/now_playing', 'page=' + str(page))
        [arr.append(obj(**res)) for res in result['results']]
        return arr

    # Get the list of top rated movies. By default, this list will only include movies that have 50 or more votes.
    # This list refreshes every day.
    def top_rated(self, page=1):
        arr = []
        result = self._call('movie/top_rated', 'page=' + str(page))
        [arr.append(obj(**res)) for res in result['results']]
        return arr

    # Get the list of upcoming movies by release date. This list refreshes every day.
    def upcoming(self, page=1):
        arr = []
        result = self._call('movie/upcoming', 'page=' + str(page))
        [arr.append(obj(**res)) for res in result['results']]
        return arr

    # Get the list of popular movies on The Movie Database. This list refreshes every day.
    def popular(self, page=1):
        arr = []
        result = self._call('movie/popular', 'page=' + str(page))
        [arr.append(obj(**res)) for res in result['results']]
        return arr

    # Search for movies by title.
    def search(self, term, page=1):
        arr = []
        result = self._call('search/movie', 'query=' + quote_plus(term) + '&page=' + str(page))
        [arr.append(obj(**res)) for res in result['results']]
        return arr

    # Get the similar movies for a specific movie id.
    def similar(self, id, page=1):
        arr = []
        result = self._call('movie/' + str(id) + '/similar', 'page=' + str(page))
        [arr.append(obj(**res)) for res in result['results']]
        return arr

    # Get the primary information about a TV series by id.
    def get_tv_show(self, show_id, append_to_response="append_to_response=trailers,images,casts,translations"):
        return obj(**self._call('tv/' + str(show_id), append_to_response))

    # Get the latest TV show id.
    def get_latest_tv_show(self):
        return obj(**self._call('tv/latest', ''))

    # Search for TV shows by title.
    def search_tv(self, term, page=1):
        arr = []
        result = self._call('search/tv', 'query=' + quote_plus(term) + '&page=' + str(page))
        [arr.append(obj(**res)) for res in result['results']]
        return arr

    # Get the similar TV shows for a specific tv id.
    def similar_shows(self, id, page=1):
        arr = []
        result = self._call('tv/' + str(id) + '/similar', 'page=' + str(page))
        [arr.append(obj(**res)) for res in result['results']]
        return arr

    # Get the list of popular TV shows. This list refreshes every day.
    def popular_shows(self, page=1):
        arr = []
        result = self._call('tv/popular', 'page=' + str(page))
        [arr.append(obj(**res)) for res in result['results']]
        return arr

    # Get the list of top rated TV shows.
    # By default, this list will only include TV shows that have 2 or more votes.
    # This list refreshes every day.

    def top_rated_shows(self, page=1):
        arr = []
        result = self._call('tv/top_rated', 'page=' + str(page))
        [arr.append(obj(**res)) for res in result['results']]
        return arr

    # Get the general person information for a specific id.
    def get_person(self, id):
        return obj(**self._call('person/' + str(id), ''))

    # Search for people by name.
    def search_person(self, term, page=1):
        arr = []
        result = self._call('search/person', 'query=' + quote_plus(term) + '&page=' + str(page))
        [arr.append(obj(**res)) for res in result['results']]
        return arr

    # Raise a custom TMDb exception if the status code of the response isn't 200.
    @staticmethod
    def raise_tmdb_exception(status_code):
        exceptions = [
            {
                'id': 34,
                'status': 'The resource you requested could not be found.'
            }
        ]

        for exception in exceptions:
            if exception['id'] == status_code:
                raise Exception(exception['status'])

        # If the exception status isn't found, just raise an empty exception.
        raise Exception('An error occurred when making that request.')

    def _call(self, action, append_to_response):
        url = '%s%s?api_key=%s&%s&language=%s' % (self.URL, action, self.api_key, append_to_response, self.lang)
        response = urlopen(url)
        data = json.loads(response.read())
        if 'status_code' in data and 'status_code' != 200:
            self.raise_tmdb_exception(data['status_code'])
        if self.debug:
            pprint.pprint(data)
            print 'URL: ' + url
        return data
