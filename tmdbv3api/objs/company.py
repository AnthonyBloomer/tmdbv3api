from tmdbv3api.tmdb import TMDb
from tmdbv3api.as_obj import AsObj


class Company(TMDb):
    _urls = {
        'details': '/company/%s',
        'movies': '/company/%s/movies'
    }

    def details(self, company_id):
        """
        Get a companies details by id.
        :param company_id: int
        :return:
        """
        return AsObj(**self._call(self._urls['details'] % str(company_id), ''))

    def movies(self, company_id):
        """
        Get the movies of a company by id.
        :param company_id: int
        :return:
        """
        return self._get_obj(self._call(self._urls['movies'] % str(company_id), ''))
