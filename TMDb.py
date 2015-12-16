import json
import pprint
from urllib import quote_plus, urlopen


class Movie:
    movie_data = []

    def __init__(self, movie_data):
        self.movie_data = movie_data

    def get_id(self):
        return self.movie_data['id']

    def get_title(self):
        return self.movie_data['title']

    def get_overview(self):
        return self.movie_data['overview']

    def get_poster(self):
        return self.movie_data['poster_path']

    def get_vote_average(self):
        return self.movie_data['vote_average']

    def get_vote_count(self):
        return self.movie_data['vote_count']

    def get_popularity(self):
        return self.movie_data['popularity']

    def get_release_date(self):
        return self.movie_data['release_date']

    def get_original_language(self):
        return self.movie_data['original_language']

    def get_original_title(self):
        return self.movie_data['original_title']


class TMDb:
    URL = "http://api.themoviedb.org/3/"

    api_key = ""
    debug = False
    lang = "en"

    config = []

    def __init__(self, apikey, debug):
        self.set_key(apikey)
        self.set_debug(debug)
        self.set_config()

    def set_config(self):
        self.config = self._call('configuration', '')

    def get_config(self):
        return self.config

    def get_image_url(self, size='original'):
        return self.config['images']['base_url'] + size

    def set_key(self, apikey):
        self.api_key = apikey

    def get_key(self):
        return self.api_key

    def set_debug(self, debug):
        self.debug = debug

    def get_debug(self):
        return self.debug

    def get_movie(self, movie_id, append_to_response="append_to_response=trailers,images,casts,translations"):
        return Movie(self._call('movie/' + movie_id, append_to_response))

    def now_playing(self, page=1):
        movies = []
        result = self._call('movie/now-playing', 'page=' + str(page))
        [movies.append(Movie(res)) for res in result['results']]
        return movies

    def top_rated(self, page=1):
        movies = []
        result = self._call('movie/top-rated', 'page=' + str(page))
        [movies.append(Movie(res)) for res in result['results']]
        return movies

    def upcoming(self, page=1):
        movies = []
        result = self._call('movie/upcoming', 'page=' + str(page))
        [movies.append(Movie(res)) for res in result['results']]
        return movies

    def popular(self, page=1):
        movies = []
        result = self._call('movie/popular', 'page=' + str(page))
        [movies.append(Movie(res)) for res in result['results']]
        return movies

    def search(self, term):
        movies = []
        result = self._call('search/movie', 'query=' + quote_plus(term))
        [movies.append(Movie(res)) for res in result['results']]
        return movies

    def _call(self, action, append_to_response):
        url = self.URL + action + '?api_key=' + self.api_key + '&' + append_to_response

        response = urlopen(url)

        data = json.loads(response.read())

        if self.debug:
            pprint.pprint(data)
            print 'URL: ' + url

        return data
