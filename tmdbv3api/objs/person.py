import warnings
from tmdbv3api.tmdb import TMDb
from .search import Search


class Person(TMDb):
    _urls = {
        "details": "/person/%s",
        "movie_credits": "/person/%s/movie_credits",
        "tv_credits": "/person/%s/tv_credits",
        "combined_credits": "/person/%s/combined_credits",
        "images": "/person/%s/images",
        "latest": "/person/latest",
        "popular": "/person/popular",
        "search_people": "/search/person",
    }

    def details(self, person_id, append_to_response="videos,images"):
        """
        Get the primary person details by id.
        :param append_to_response: str
        :param person_id: int
        :return:
        """
        return self._request_obj(
            self._urls["details"] % person_id,
            params="append_to_response=%s" % append_to_response
        )

    def movie_credits(self, person_id):
        """
        Get the movie credits for a person.
        :param person_id: int
        :return:
        """
        return self._request_obj(self._urls["movie_credits"] % person_id)

    def tv_credits(self, person_id):
        """
        Get the TV show credits for a person.
        :param person_id: int
        :return:
        """
        return self._request_obj(self._urls["tv_credits"] % person_id)

    def combined_credits(self, person_id):
        """
        Get the movie and TV credits together in a single response.
        :param person_id: int
        :return:
        """
        return self._request_obj(self._urls["combined_credits"] % person_id)

    def images(self, person_id):
        """
        Get the images for a person.
        :param person_id: int
        :return:
        """
        return self._request_obj(
            self._urls["images"] % person_id,
            key="profiles"
        )

    def latest(self):
        """
        Get the most newly created person. This is a live response and will continuously change.
        :return:
        """
        return self._request_obj(self._urls["latest"])

    def popular(self, page=1):
        """
        Get the list of popular people on TMDb. This list updates daily.
        :param page: int
        :return:
        """
        return self._request_obj(
            self._urls["popular"],
            params="page=%s" % page,
            key="results"
        )

    def search(self, term, page=1):
        """
        Search for people.
        :param term: string
        :param page: int
        :return:
        """
        warnings.warn("search method is deprecated use tmdbv3api.Search().people(params)",
                      DeprecationWarning)
        return Search().people(term, page=page)
