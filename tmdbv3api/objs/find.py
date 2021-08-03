from tmdbv3api.tmdb import TMDb


class Find(TMDb):
    _find_url = "/find/%s"

    def find(self, external_id, external_source):
        """
        The find method makes it easy to search for objects in our database by an external id. For example, an IMDB ID.
        :param external_id: str
        :param external_source str
        :return:
        """
        return self._get_obj(
            self._call(
                self._find_url % external_id,
                "external_source=" + external_source,
            ),
            key=None,
        )

    def find_by_imdb_id(self, imdb_id):
        """
        The find method makes it easy to search for objects in our database by an IMDB ID.
        :param imdb_id: str
        :return:
        """
        return self.find(imdb_id, "imdb_id")

    def find_by_tvdb_id(self, tvdb_id):
        """
        The find method makes it easy to search for objects in our database by a TVDB ID.
        :param tvdb_id: str
        :return:
        """
        return self.find(tvdb_id, "tvdb_id")