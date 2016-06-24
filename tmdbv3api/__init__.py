import json
import pprint
from urllib import quote_plus, urlopen


class TVShow:
    tvdata = []

    def __init__(self, tvdata):
        self.tvdata = tvdata

    def id(self):
        return self.tvdata['id']

    def name(self):
        return self.tvdata['name']

    def overview(self):
        return self.tvdata['overview']

    def first_air_date(self):
        return self.tvdata['first_air_date']

    def last_air_date(self):
        return self.tvdata['last_air_date']

    def number_of_episodes(self):
        return self.tvdata['number_of_episodes']

    def number_of_seasons(self):
        return self.tvdata['number_of_seasons']

    def poster(self):
        return self.tvdata['poster_path']

    def backdrop_path(self):
        return self.tvdata['backdrop_path']

    def vote_average(self):
        return self.tvdata['vote_average']

    def vote_count(self):
        return self.tvdata['vote_count']

    def popularity(self):
        return self.tvdata['popularity']

    def release_date(self):
        return self.tvdata['release_date']

    def original_language(self):
        return self.tvdata['original_language']

    def original_name(self):
        return self.tvdata['original_name']

    def status(self):
        return self.tvdata['status']

    def type(self):
        return self.tvdata['type']

    def json(self):
        return json.dumps(self.tvdata)


class Person:
    persondata = []

    def __init__(self, persondata):
        self.persondata = persondata

    def id(self):
        return self.persondata['id']

    def name(self):
        return self.persondata['name']

    def biography(self):
        return self.persondata['biography']

    def birthday(self):
        return self.persondata['birthday']

    def deathday(self):
        return self.persondata['deathday']

    def profilepath(self):
        return self.persondata['profile_path']

    def place_of_birth(self):
        return self.persondata['place_of_birth']

    def homepage(self):
        return self.persondata['homepage']

    def json(self):
        return json.dumps(self.persondata)


class Movie:
    movie_data = []

    def __init__(self, movie_data):
        self.movie_data = movie_data

    def id(self):
        return self.movie_data['id']

    def adult(self):
        return self.movie_data['adult']

    def title(self):
        return self.movie_data['title']

    def overview(self):
        return self.movie_data['overview']

    def poster(self):
        return self.movie_data['poster_path']

    def backdrop_path(self):
        return self.movie_data['backdrop_path']

    def vote_average(self):
        return self.movie_data['vote_average']

    def vote_count(self):
        return self.movie_data['vote_count']

    def popularity(self):
        return self.movie_data['popularity']

    def release_date(self):
        return self.movie_data['release_date']

    def original_language(self):
        return self.movie_data['original_language']

    def original_title(self):
        return self.movie_data['original_title']

    def revenue(self):
        return self.movie_data['revenue']

    def belongs_to_collection(self):
        return self.movie_data['belongs_to_collection']

    def json(self):
        return json.dumps(self.movie_data)


# http://docs.themoviedb.apiary.io
class TMDb:
    URL = "http://api.themoviedb.org/3/"

    def __init__(self, api_key, debug=False, lang='en'):
        self.api_key = api_key
        self.debug = debug
        self.lang = lang
        self._set_config()
        self.data = []

    def _set_config(self):
        self.config = self._call('configuration', '')

    def get_config(self):
        return self.config

    # Get the basic movie information for a specific movie id.
    def get_movie(self, movie_id, append_to_response="append_to_response=trailers,images,casts,translations"):
        return Movie(self._call('movie/' + str(movie_id), append_to_response))

    # Get the latest movie id.
    def get_latest_movie(self):
        return Movie(self._call('movie/latest', ''))

    # Get the list of movies playing that have been, or are being released this week. This list refreshes every day.
    def now_playing(self, page=1):
        result = self._call('movie/now_playing', 'page=' + str(page))
        [self.data.append(Movie(res)) for res in result['results']]
        return self.data

    # Get the list of top rated movies. By default, this list will only include movies that have 50 or more votes.
    # This list refreshes every day.
    def top_rated(self, page=1):
        result = self._call('movie/top_rated', 'page=' + str(page))
        [self.data.append(Movie(res)) for res in result['results']]
        return self.data

    # Get the list of upcoming movies by release date. This list refreshes every day.
    def upcoming(self, page=1):
        result = self._call('movie/upcoming', 'page=' + str(page))
        [self.data.append(Movie(res)) for res in result['results']]
        return self.data

    # Get the list of popular movies on The Movie Database. This list refreshes every day.
    def popular(self, page=1):
        result = self._call('movie/popular', 'page=' + str(page))
        [self.data.append(Movie(res)) for res in result['results']]
        return self.data

    # Search for movies by title.
    def search(self, term, page=1):
        result = self._call('search/movie', 'query=' + quote_plus(term) + '&page=' + str(page))
        [self.data.append(Movie(res)) for res in result['results']]
        return self.data

    # Get the similar movies for a specific movie id.
    def similar(self, id, page=1):
        result = self._call('movie/' + str(id) + '/similar', 'page=' + str(page))
        [self.data.append(Movie(res)) for res in result['results']]
        return self.data

    # Get the primary information about a TV series by id.
    def get_tv_show(self, show_id, append_to_response="append_to_response=trailers,images,casts,translations"):
        return TVShow(self._call('tv/' + str(show_id), append_to_response))

    # Get the latest TV show id.
    def get_latest_tv_show(self):
        return TVShow(self._call('tv/latest', ''))

    # Search for TV shows by title.
    def search_tv(self, term, page=1):
        result = self._call('search/tv', 'query=' + quote_plus(term) + '&page=' + str(page))
        [self.data.append(TVShow(res)) for res in result['results']]
        return self.data

    # Get the similar TV shows for a specific tv id.
    def similar_shows(self, id, page=1):
        result = self._call('tv/' + str(id) + '/similar', 'page=' + str(page))
        [self.data.append(TVShow(res)) for res in result['results']]
        return self.data

    # Get the list of popular TV shows. This list refreshes every day.
    def popular_shows(self, page=1):
        result = self._call('tv/popular', 'page=' + str(page))
        [self.data.append(TVShow(res)) for res in result['results']]
        return self.data

    # Get the list of top rated TV shows.
    # By default, this list will only include TV shows that have 2 or more votes.
    # This list refreshes every day.

    def top_rated_shows(self, page=1):
        result = self._call('tv/top_rated', 'page=' + str(page))
        [self.data.append(TVShow(res)) for res in result['results']]
        return self.data

    # Get the general person information for a specific id.
    def get_person(self, id):
        return Person(self._call('person/' + str(id), ''))

    # Search for people by name.
    def search_person(self, term, page=1):
        result = self._call('search/person', 'query=' + quote_plus(term) + '&page=' + str(page))
        [self.data.append(Person(res)) for res in result['results']]
        return self.data

    def _call(self, action, append_to_response):
        url = self.URL + action + '?api_key=' + self.api_key + '&' + append_to_response + '&language=' + self.lang
        response = urlopen(url)
        data = json.loads(response.read())
        if self.debug:
            pprint.pprint(data)
            print 'URL: ' + url
        return data
