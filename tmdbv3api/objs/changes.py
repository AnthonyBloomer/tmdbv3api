from tmdbv3api.tmdb import TMDb


class Changes(TMDb):
    _urls = {
        "movie": "/movie/changes",
        "tv": "/tv/changes",
        "person": "/person/changes"
    }

    def _changes(self, change_type, start_date="", end_date="", page=1):
        params = "page=%s" % page
        if start_date:
            params += "&start_date=%s" % start_date
        if end_date:
            params += "&end_date=%s" % end_date
        return self._request_obj(
            self._urls[change_type],
            params=params,
            key="results"
        )

    def movie_changes(self, start_date="", end_date="", page=1):
        """
        Get the changes for a movie. By default only the last 24 hours are returned.
        You can query up to 14 days in a single query by using the start_date and end_date query parameters.
        :param start_date: str
        :param end_date: str
        :param page: int
        :return:
        """
        return self._changes("movie", start_date=start_date, end_date=end_date, page=page)

    def tv_changes(self, start_date="", end_date="", page=1):
        """
        Get a list of all of the TV show ids that have been changed in the past 24 hours.
        You can query up to 14 days in a single query by using the start_date and end_date query parameters.
        :param start_date: str
        :param end_date: str
        :param page: int
        :return:
        """
        return self._changes("tv", start_date=start_date, end_date=end_date, page=page)

    def person_changes(self, start_date="", end_date="", page=1):
        """
        Get a list of all of the person ids that have been changed in the past 24 hours.
        You can query up to 14 days in a single query by using the start_date and end_date query parameters.
        :param start_date: str
        :param end_date: str
        :param page: int
        :return:
        """
        return self._changes("person", start_date=start_date, end_date=end_date, page=page)
