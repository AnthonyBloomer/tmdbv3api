from tmdbv3api.tmdb import TMDb
from tmdbv3api.as_obj import AsObj

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote


class TV(TMDb):
    URLS = {
        'details': '/tv/%s',
        'latest': '/tv/latest',
        'search_tv': '/search/tv',
        'popular': '/tv/popular',
        'top_rated': '/tv/top_rated',
        'similar': '/tv/%s/similar'
    }

    def details(self, show_id, append_to_response="append_to_response=trailers,images,casts,translations"):
        """
        Get the primary TV show details by id.
        :param show_id:
        :param append_to_response:
        :return:
        """
        return AsObj(**self._call(self.URLS['details'] % str(show_id), append_to_response))

    def latest(self):
        """
        Get the most newly created TV show. This is a live response and will continuously change.
        :return:
        """
        return AsObj(**self._call(self.URLS['latest'], ''))

    def search(self, term, page=1):
        """
        Search for a TV show.
        :param term:
        :param page:
        :return:
        """
        return self._get_obj(self._call(self.URLS['search_tv'], 'query=' + quote(term) + '&page=' + str(page)))

    def similar(self, id, page=1):
        """
        Get the primary TV show details by id.
        :param id:
        :param page:
        :return:
        """
        return self._get_obj(self._call(self.URLS['similar'] % str(id), 'page=' + str(page)))

    def popular(self, page=1):
        """
        Get a list of the current popular TV shows on TMDb. This list updates daily.
        :param page:
        :return:
        """
        return self._get_obj(self._call(self.URLS['popular'], 'page=' + str(page)))

    def top_rated(self, page=1):
        """
        Get a list of the top rated TV shows on TMDb.
        :param page:
        :return:
        """
        return self._get_obj(self._call(self.URLS['top_rated'], 'page=' + str(page)))
