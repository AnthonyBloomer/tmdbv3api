from tmdbv3api.tmdb import TMDb
from tmdbv3api.as_obj import AsObj

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote


class Movie(TMDb):
    _urls = {
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
        'similar': '/movie/%s/similar',
        'credits': '/movie/%s/credits',
        'images': '/movie/%s/images',
        'keywords': '/movie/%s/keywords',
        'external': '/find/%s',
        'external_ids': '/movie/%s/external_ids',
    }

    def keywords(self, movie_id):
        """
        Get the keywords associated to a movie.
        :param movie_id:
        :return:
        """
        return self._get_obj(self._call(self._urls['keywords'] % movie_id, ''), 'keywords')

    def details(self, movie_id, append_to_response='videos,trailers,images,casts,translations,keywords'):
        """
        Get the primary information about a movie.
        :param movie_id:
        :param append_to_response:
        :return:
        """
        return AsObj(**self._call(self._urls['details'] % movie_id, 'append_to_response=' + append_to_response))

    def credits(self, movie_id):
        """
        Get the cast and crew for a movie.
        :param movie_id:
        :return:
        """
        return AsObj(**self._call(self._urls['credits'] % movie_id, ''))

    def reviews(self, movie_id, page=1):
        """
        Get the user reviews for a movie.
        :param movie_id:
        :param page:
        :return:
        """
        return self._get_obj(self._call(self._urls['reviews'] % movie_id, 'page=' + str(page)))

    def lists(self, movie_id, page=1):
        """
        Get a list of lists that this movie belongs to.
        :param movie_id:
        :param page:
        :return:
        """
        return self._get_obj(self._call(self._urls['lists'] % movie_id, 'page=' + str(page)))

    def videos(self, id, page=1):
        """
        Get the videos that have been added to a movie.
        :param id:
        :param page:
        :return:
        """
        return self._get_obj(self._call(self._urls['videos'] % id, 'page=' + str(page)))

    def recommendations(self, movie_id, page=1):
        """
        Get a list of recommended movies for a movie.
        :param movie_id:
        :param page:
        :return:
        """
        return self._get_obj(self._call(self._urls['recommendations'] % movie_id, 'page=' + str(page)))

    def latest(self):
        """
        Get the most newly created movie. This is a live response and will continuously change.
        :return:
        """
        return AsObj(**self._call(self._urls['latest'], ''))

    def now_playing(self, page=1):
        """
        Get a list of movies in theatres.
        :param page:
        :return:
        """
        return self._get_obj(self._call(self._urls['now_playing'], 'page=' + str(page)))

    def top_rated(self, page=1):
        """
        Get the top rated movies on TMDb.
        :param page:
        :return:
        """
        return self._get_obj(self._call(self._urls['top_rated'], 'page=' + str(page)))

    def upcoming(self, page=1):
        """
        Get a list of upcoming movies in theatres.
        :param page:
        :return:
        """
        return self._get_obj(self._call(self._urls['upcoming'], 'page=' + str(page)))

    def popular(self, page=1):
        """
        Get a list of the current popular movies on TMDb. This list updates daily.
        :param page:
        :return:
        """
        return self._get_obj(self._call(self._urls['popular'], 'page=' + str(page)))

    def search(self, term, page=1):
        """
        Search for movies.
        :param term:
        :param page:
        :return:
        """
        return self._get_obj(self._call(self._urls['search_movie'], "query=" + quote(term) + "&page=" + str(page)))

    def similar(self, movie_id, page=1):
        """
        Get a list of similar movies.
        :param movie_id:
        :param page:
        :return:
        """
        return self._get_obj(self._call(self._urls['similar'] % movie_id, 'page=' + str(page)))

    def external(self, external_id, external_source):
        """
        The find method makes it easy to search for objects in our database by an external id. For example, an IMDB ID.
        :param external_id: str
        :param external_source str
        :return:
        """
        return self._get_obj(self._call(self._urls['external'] % external_id, 'external_source=' + external_source),
                             key=None)

    def images(self, movie_id):
        """
        Get the images that belong to a movie.
        :param movie_id:
        :return:
        """
        return AsObj(**self._call(self._urls['images'] % movie_id, ''))

    def external_ids(self, movie_id):
        """
        Get the external ids for a movie.
        :param movie_id:
        :return:
        """
        return self._get_obj(self._call(self._urls['external_ids'] % (str(movie_id)), ''), None)
