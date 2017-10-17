from tmdbv3api.tmdb import TMDb
from tmdbv3api.endpoints import Endpoint

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode


class Discover(TMDb):
    def discover_movies(self, params):
        """
        Discover movies by different types of data like average rating, number of votes, genres and certifications.
        :param params:
        :return:
        """
        return self._get_obj(self._call(Endpoint.DISCOVER_MOVIES, urlencode(params)))

    def discover_tv_shows(self, params):
        """
        Discover TV shows by different types of data like average rating, number of votes, genres,
        the network they aired on and air dates.
        :param params:
        :return:
        """
        return self._get_obj(self._call(Endpoint.DISCOVER_TV, urlencode(params)))
