from tmdbv3api.tmdb import TMDb
from tmdbv3api.as_obj import AsObj
from tmdbv3api.endpoints import Endpoint

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote


class TV(TMDb):
    def get_tv_show(self, show_id, append_to_response="append_to_response=trailers,images,casts,translations"):
        """
        Get the primary TV show details by id.
        :param show_id:
        :param append_to_response:
        :return:
        """
        return AsObj(**self._call(Endpoint.TV_SHOW % str(show_id), append_to_response))

    def get_latest_tv_show(self):
        """
        Get the most newly created TV show. This is a live response and will continuously change.
        :return:
        """
        return AsObj(**self._call(Endpoint.TV_LATEST, ''))

    def search_tv(self, term, page=1):
        """
        Search for a TV show.
        :param term:
        :param page:
        :return:
        """
        return self._get_obj(self._call(Endpoint.SEARCH_TV, 'query=' + quote(term) + '&page=' + str(page)))

    def similar_shows(self, id, page=1):
        """
        Get the primary TV show details by id.
        :param id:
        :param page:
        :return:
        """
        return self._get_obj(self._call(Endpoint.TV_SIMILAR % id, 'page=' + str(page)))

    def popular_shows(self, page=1):
        """
        Get a list of the current popular TV shows on TMDb. This list updates daily.
        :param page:
        :return:
        """
        return self._get_obj(self._call(Endpoint.TV_POPULAR, 'page=' + str(page)))

    def top_rated_shows(self, page=1):
        """
        Get a list of the top rated TV shows on TMDb.
        :param page:
        :return:
        """
        return self._get_obj(self._call(Endpoint.TV_TOP_RATED, 'page=' + str(page)))
