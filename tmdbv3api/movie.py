from tmdbv3api.tmdb import TMDb
from tmdbv3api.endpoints import Endpoint
from tmdbv3api.as_obj import AsObj
from urllib import quote_plus


class Movie(TMDb):
    def get_movie(self, movie_id, append_to_response="append_to_response=trailers,images,casts,translations"):
        """
        Get the primary information about a movie.
        :param movie_id:
        :param append_to_response:
        :return:
        """
        return AsObj(**self._call(Endpoint.MOVIE + str(movie_id), append_to_response))

    def get_movie_reviews(self, id, page=1):
        """
        Get the user reviews for a movie.
        :param id:
        :param page:
        :return:
        """
        return self._get_obj(self._call(Endpoint.MOVIE_REVIEWS % id, 'page=' + str(page)))

    def get_movie_lists(self, id, page=1):
        """
        Get a list of lists that this movie belongs to.
        :param id:
        :param page:
        :return:
        """
        return self._get_obj(self._call(Endpoint.MOVIE_LISTS % id, 'page=' + str(page)))

    def get_movie_videos(self, id, page=1):
        """
        Get the videos that have been added to a movie.
        :param id:
        :param page:
        :return:
        """
        return self._get_obj(self._call(Endpoint.MOVIE_VIDEOS % id, 'page=' + str(page)))

    def get_movie_recommendations(self, movie_id, page=1):
        """
        Get a list of recommended movies for a movie.
        :param movie_id:
        :param page:
        :return:
        """
        return self._get_obj(self._call(Endpoint.MOVIE_RECOMMENDATIONS % movie_id, 'page=' + str(page)))

    def get_latest_movie(self):
        """
        Get the most newly created movie. This is a live response and will continuously change.
        :return:
        """
        return AsObj(**self._call(Endpoint.MOVIE_LATEST, ''))

    def now_playing(self, page=1):
        """
        Get a list of movies in theatres.
        :param page:
        :return:
        """
        return self._get_obj(self._call(Endpoint.NOW_PLAYING, 'page=' + str(page)))

    def top_rated(self, page=1):
        """
        Get the top rated movies on TMDb.
        :param page:
        :return:
        """
        return self._get_obj(self._call(Endpoint.TOP_RATED, 'page=' + str(page)))

    def upcoming(self, page=1):
        """
        Get a list of upcoming movies in theatres.
        :param page:
        :return:
        """
        return self._get_obj(self._call(Endpoint.UPCOMING, 'page=' + str(page)))

    def popular(self, page=1):
        """
        Get a list of the current popular movies on TMDb. This list updates daily.
        :param page:
        :return:
        """
        return self._get_obj(self._call(Endpoint.POPULAR, 'page=' + str(page)))

    def search(self, term, page=1):
        """
        Search for movies.
        :param term:
        :param page:
        :return:
        """
        return self._get_obj(self._call(Endpoint.SEARCH_MOVIE, "query=" + quote_plus(term) + "&page=" + str(page)))

    def similar(self, id, page=1):
        """
        Get a list of similar movies.
        :param id:
        :param page:
        :return:
        """
        return self._get_obj(self._call(Endpoint.MOVIE_SIMILAR % id, 'page=' + str(page)))
