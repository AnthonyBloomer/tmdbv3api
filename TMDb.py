import json
import pprint
from urllib import quote_plus, urlopen
from Movie import Movie


class TMDb:
    URL = "http://api.themoviedb.org/3/"

    api_key = ''
    debug = False
    lang = ''

    config = []

    current_page = 0
    total_pages = 0

    def __init__(self, apikey, debug=False, language='en'):
        self._set_key(apikey)
        self._set_debug(debug)
        self._set_lang(language)
        self._set_config()

    def _set_config(self):
        self.config = self._call('configuration', '')

    def get_config(self):
        return self.config

    def get_image_url(self, size='original'):
        return self.config['images']['base_url'] + size

    def _set_lang(self, lang):
        self.lang = lang

    def _get_lang(self):
        return self.lang

    def _set_key(self, apikey):
        self.api_key = apikey

    def _get_key(self):
        return self.api_key

    def _set_debug(self, debug):
        self.debug = debug

    def _get_debug(self):
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
        self.total_pages = result['total_pages']
        self.current_page = result['page']
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
        self.total_pages = result['total_pages']
        self.current_page = result['page']
        return movies

    def popular(self, page=1):
        movies = []
        result = self._call('movie/popular', 'page=' + str(page))
        [movies.append(Movie(res)) for res in result['results']]
        self.total_pages = result['total_pages']
        self.current_page = result['page']
        return movies

    def search(self, term, page=1):
        movies = []
        result = self._call('search/movie', 'query=' + quote_plus(term) + '&page=' + str(page))
        [movies.append(Movie(res)) for res in result['results']]
        self.total_pages = result['total_pages']
        self.current_page = result['page']
        return movies

    def similar(self, id, page=1):
        movies = []
        result = self._call('movie/' + str(id) + '/similar', 'page=' + str(page))
        [movies.append(Movie(res)) for res in result['results']]
        self.total_pages = result['total_pages']
        self.current_page = result['page']
        return movies

    def _call(self, action, append_to_response):
        url = self.URL + action + '?api_key=' + self.api_key + '&' + append_to_response + '&language=' + self.lang

        response = urlopen(url)

        data = json.loads(response.read())

        if self.debug:
            pprint.pprint(data)
            print 'URL: ' + url

        return data
