from tmdbv3api.tmdb import TMDb


class Network(TMDb):
    _urls = {
        "details": "/network/%s",
        "alternative_names": "/network/%s/alternative_names",
        "images": "/network/%s"
    }

    def details(self, network_id):
        """
        Get a networks details by id.
        :param network_id: int
        :return:
        """
        return self._request_obj(self._urls["details"] % network_id)
