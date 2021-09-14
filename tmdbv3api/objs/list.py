from tmdbv3api.tmdb import TMDb


class List(TMDb):
    _urls = {"details": "/list/%s"}

    def details(self, list_id):
        """
        Get list details by id.
        :param list_id: int
        :return:
        """
        return self._request_obj(self._urls["details"] % list_id)
