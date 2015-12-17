import json
import pprint
from urllib import quote_plus, urlopen

from Objects.Movie import Movie

from Objects.TVShow import TVShow

from Objects.Person import Person


# http://docs.themoviedb.apiary.io
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

    # Get the basic movie information for a specific movie id.
    def get_movie(self, movie_id, append_to_response="append_to_response=trailers,images,casts,translations"):
        return Movie(self._call('movie/' + str(movie_id), append_to_response))

    # Get the latest movie id.
    def get_latest_movie(self):
        return Movie(self._call('movie/latest', ''))

    # Get the list of movies playing that have been, or are being released this week. This list refreshes every day.
    def now_playing(self, page=1):
        movies = []
        result = self._call('movie/now-playing', 'page=' + str(page))
        [movies.append(Movie(res)) for res in result['results']]
        self.total_pages = result['total_pages']
        self.current_page = result['page']
        return movies

    # Get the list of top rated movies. By default, this list will only include movies that have 50 or more votes.
    # This list refreshes every day.
    def top_rated(self, page=1):
        movies = []
        result = self._call('movie/top-rated', 'page=' + str(page))
        [movies.append(Movie(res)) for res in result['results']]
        self.total_pages = result['total_pages']
        self.current_page = result['page']
        return movies

    # Get the list of upcoming movies by release date. This list refreshes every day.
    def upcoming(self, page=1):
        movies = []
        result = self._call('movie/upcoming', 'page=' + str(page))
        [movies.append(Movie(res)) for res in result['results']]
        self.total_pages = result['total_pages']
        self.current_page = result['page']
        return movies

    # Get the list of popular movies on The Movie Database. This list refreshes every day.
    def popular(self, page=1):
        movies = []
        result = self._call('movie/popular', 'page=' + str(page))
        [movies.append(Movie(res)) for res in result['results']]
        self.total_pages = result['total_pages']
        self.current_page = result['page']
        return movies

    # Search for movies by title.
    def search(self, term, page=1):
        movies = []
        result = self._call('search/movie', 'query=' + quote_plus(term) + '&page=' + str(page))
        [movies.append(Movie(res)) for res in result['results']]
        self.total_pages = result['total_pages']
        self.current_page = result['page']
        return movies

    # Get the similar movies for a specific movie id.
    def similar(self, id, page=1):
        movies = []
        result = self._call('movie/' + str(id) + '/similar', 'page=' + str(page))
        [movies.append(Movie(res)) for res in result['results']]
        self.total_pages = result['total_pages']
        self.current_page = result['page']
        return movies

    # Get the primary information about a TV series by id.
    def get_tv_show(self, show_id, append_to_response="append_to_response=trailers,images,casts,translations"):
        return TVShow(self._call('tv/' + str(show_id), append_to_response))

    # Get the latest TV show id.
    def get_latest_tv_show(self):
        return TVShow(self._call('tv/latest', ''))

    # Search for TV shows by title.
    def search_tv(self, term, page=1):
        shows = []
        result = self._call('search/tv', 'query=' + quote_plus(term) + '&page=' + str(page))
        [shows.append(TVShow(res)) for res in result['results']]
        self.total_pages = result['total_pages']
        self.current_page = result['page']
        return shows

    # Get the similar TV shows for a specific tv id.
    def similar_shows(self, id, page=1):
        shows = []
        result = self._call('tv/' + str(id) + '/similar', 'page=' + str(page))
        [shows.append(TVShow(res)) for res in result['results']]
        self.total_pages = result['total_pages']
        self.current_page = result['page']
        return shows

    # Get the general person information for a specific id.
    def get_person(self, id, append_to_response="append_to_response=trailers,images,casts,translations"):
        return Person(self._call('person/' + str(id), append_to_response))

    # Search for people by name.
    def search_person(self, term, page=1):
        people = []
        result = self._call('search/person', 'query=' + quote_plus(term) + '&page=' + str(page))
        [people.append(Person(res)) for res in result['results']]
        self.total_pages = result['total_pages']
        self.current_page = result['page']
        return people

    def _call(self, action, append_to_response):
        url = self.URL + action + '?api_key=' + self.api_key + '&' + append_to_response + '&language=' + self.lang

        response = urlopen(url)

        data = json.loads(response.read())

        if self.debug:
            pprint.pprint(data)
            print 'URL: ' + url

        return data
