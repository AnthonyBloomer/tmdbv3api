import json
import pprint
from urllib import quote_plus, urlopen
from Movie import Movie


class TMDb:
    URL = "http://api.themoviedb.org/3/"

    api_key = ""
    debug = False
    lang = "en"

    config = []

    current_page = 0
    total_pages = 0

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

    def get_total_pages(self):
        return self.total_pages

    def get_current_page(self):
        return self.current_page

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
        self.total_pages = result['total_pages']
        self.current_page = result['page']
        return movies

    def upcoming(self, page=1):
        movies = []
        result = self._call('movie/upcoming', 'page=' + str(page))
        [movies.append(Movie(res)) for res in result['results']]
        print result['total_pages']
        print result['page']
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
        print result['total_pages']
        print result['page']
        return movies

    def _call(self, action, append_to_response):
        url = self.URL + action + '?api_key=' + self.api_key + '&' + append_to_response

        response = urlopen(url)

        data = json.loads(response.read())

        if self.debug:
            pprint.pprint(data)
            print 'URL: ' + url

        return data
