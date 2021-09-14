import warnings
from tmdbv3api.tmdb import TMDb
from .search import Search

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote


class TV(TMDb):
    _urls = {
        "details": "/tv/%s",
        "external_ids": "/tv/%s/external_ids",
        "keywords": "/tv/%s/keywords",
        "recommendations": "/tv/%s/recommendations",
        "reviews": "/tv/%s/reviews",
        "screened_theatrically": "/tv/%s/screened_theatrically",
        "similar": "/tv/%s/similar",
        "videos": "/tv/%s/videos",
        "latest": "/tv/latest",
        "airing_today": "/tv/airing_today",
        "on_the_air": "/tv/on_the_air",
        "popular": "/tv/popular",
        "top_rated": "/tv/top_rated",
    }

    def details(self, tv_id, append_to_response="videos,trailers,images,credits,translations"):
        """
        Get the primary TV show details by id.
        :param tv_id: int
        :param append_to_response: str
        :return:
        """
        return self._request_obj(
            self._urls["details"] % tv_id,
            params="append_to_response=%s" % append_to_response,
        )

    def external_ids(self, tv_id):
        """
        Get the external ids for a TV show.
        :param tv_id: int
        :return:
        """
        return self._request_obj(self._urls["external_ids"] % tv_id)

    def keywords(self, tv_id):
        """
        Get the keywords that have been added to a TV show.
        :param tv_id: int
        :return:
        """
        return self._request_obj(
            self._urls["keywords"] % tv_id,
            key="results"
        )

    def recommendations(self, tv_id, page=1):
        """
        Get the list of TV show recommendations for this item.
        :param tv_id: int
        :param page: int
        :return:
        """
        return self._request_obj(
            self._urls["recommendations"] % tv_id,
            params="page=%s" % page,
            key="results"
        )

    def reviews(self, tv_id, page=1):
        """
        Get the reviews for a TV show.
        :param tv_id: int
        :param page: int
        :return:
        """
        return self._request_obj(
            self._urls["reviews"] % tv_id,
            params="page=%s" % page,
            key="results"
        )

    def screened_theatrically(self, tv_id):
        """
        Get a list of seasons or episodes that have been screened in a film festival or theatre.
        :param tv_id: int
        :return:
        """
        return self._request_obj(
            self._urls["screened_theatrically"] % tv_id,
            key="results"
        )

    def similar(self, tv_id, page=1):
        """
        Get the primary TV show details by id.
        :param tv_id: int
        :param page: int
        :return:
        """
        return self._request_obj(
            self._urls["similar"] % tv_id,
            params="page=%s" % page,
            key="results"
        )

    def videos(self, tv_id, include_video_language=None, page=1):
        """
        Get the videos that have been added to a TV show.
        :param tv_id: int
        :param include_video_language: str
        :param page: int
        :return:
        """
        params = "page=%s" % page
        if include_video_language:
            params += "&include_video_language=%s" % include_video_language
        return self._request_obj(
            self._urls["videos"] % tv_id,
            params=params
        )

    def latest(self):
        """
        Get the most newly created TV show. This is a live response and will continuously change.
        :return:
        """
        return self._request_obj(self._urls["latest"])

    def airing_today(self, page=1):
        """
        Get a list of TV shows that are airing today.
        This query is purely day based as we do not currently support airing times.
        :param page: int
        :return:
        """
        return self._request_obj(
            self._urls["airing_today"],
            params="page=%s" % page,
            key="results"
        )

    def on_the_air(self, page=1):
        """
        Get a list of shows that are currently on the air.
        :param page:
        :return:
        """
        return self._request_obj(
            self._urls["on_the_air"],
            params="page=%s" % page,
            key="results"
        )

    def popular(self, page=1):
        """
        Get a list of the current popular TV shows on TMDb. This list updates daily.
        :param page:
        :return:
        """
        return self._request_obj(
            self._urls["popular"],
            params="page=%s" % page,
            key="results"
        )

    def top_rated(self, page=1):
        """
        Get a list of the top rated TV shows on TMDb.
        :param page:
        :return:
        """
        return self._request_obj(
            self._urls["top_rated"],
            params="page=%s" % page,
            key="results"
        )

    def search(self, term, page=1):
        """
        Search for a TV show.
        :param term:
        :param page:
        :return:
        """
        warnings.warn("search method is deprecated use tmdbv3api.Search().tv_shows(term)",
                      DeprecationWarning)
        return Search().tv_shows(term, page=page)
