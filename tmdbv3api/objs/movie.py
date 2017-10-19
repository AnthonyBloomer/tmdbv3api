from tmdbv3api.tmdb import TMDb
from tmdbv3api.as_obj import AsObj

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote


class Movie(TMDb):
    URLS = {
        'details': '/movie/%s',
        'reviews': '/movie/%s/reviews',
        'lists': '/movie/%s/lists',
        'videos': '/movie/%s/videos',
        'recommendations': '/movie/%s/recommendations',
        'latest': '/movie/latest',
        'now_playing': '/movie/now_playing',
        'top_rated': '/movie/top_rated',
        'upcoming': '/movie/upcoming',
        'popular': '/movie/popular',
        'search_movie': '/search/movie',
        'similar': '/movie/%s/similar'
    }

    def details(self, movie_id, append_to_response="append_to_response=trailers,images,casts,translations"):
        """
        Get the primary information about a movie.
        :param movie_id:
        :param append_to_response:
        :return:
        """
        return AsObj(**self._call(self.URLS['details'] % movie_id, append_to_response))

    def reviews(self, movie_id, page=1):
        """
        Get the user reviews for a movie.
        :param movie_id:
        :param page:
        :return:
        """
        return self._get_obj(self._call(self.URLS['reviews'] % movie_id, 'page=' + str(page)))

    def lists(self, movie_id, page=1):
        """
        Get a list of lists that this movie belongs to.
        :param movie_id:
        :param page:
        :return:
        """
        return self._get_obj(self._call(self.URLS['lists'] % movie_id, 'page=' + str(page)))

    def videos(self, id, page=1):
        """
        Get the videos that have been added to a movie.
        :param id:
        :param page:
        :return:
        """
        return self._get_obj(self._call(self.URLS['videos'] % id, 'page=' + str(page)))

    def recommendations(self, movie_id, page=1):
        """
        Get a list of recommended movies for a movie.
        :param movie_id:
        :param page:
        :return:
        """
        return self._get_obj(self._call(self.URLS['recommendations'] % movie_id, 'page=' + str(page)))

    def latest(self):
        """
        Get the most newly created movie. This is a live response and will continuously change.
        :return:
        """
        return AsObj(**self._call(self.URLS['latest'], ''))

    def now_playing(self, page=1):
        """
        Get a list of movies in theatres.
        :param page:
        :return:
        """
        return self._get_obj(self._call(self.URLS['now_playing'], 'page=' + str(page)))

    def top_rated(self, page=1):
        """
        Get the top rated movies on TMDb.
        :param page:
        :return:
        """
        return self._get_obj(self._call(self.URLS['top_rated'], 'page=' + str(page)))

    def upcoming(self, page=1):
        """
        Get a list of upcoming movies in theatres.
        :param page:
        :return:
        """
        return self._get_obj(self._call(self.URLS['upcoming'], 'page=' + str(page)))

    def popular(self, page=1):
        """
        Get a list of the current popular movies on TMDb. This list updates daily.
        :param page:
        :return:
        """
        return self._get_obj(self._call(self.URLS['popular'], 'page=' + str(page)))

    def search(self, term, page=1):
        """
        Search for movies.
        :param term:
        :param page:
        :return:
        """
        return self._get_obj(self._call(self.URLS['search_movie'], "query=" + quote(term) + "&page=" + str(page)))

    def similar(self, id, page=1):
        """
        Get a list of similar movies.
        :param id:
        :param page:
        :return:
        """
        return self._get_obj(self._call(self.URLS['similar'] % id, 'page=' + str(page)))
