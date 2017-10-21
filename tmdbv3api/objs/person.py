from tmdbv3api.tmdb import TMDb
from tmdbv3api.as_obj import AsObj

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote


class Person(TMDb):
    _urls = {
        'details': '/person/%s',
        'search_people': '/search/person'
    }

    def details(self, person_id):
        """
        Get the primary person details by id.
        :param person_id:
        :return:
        """
        return AsObj(**self._call(self._urls['details'] % str(person_id), ''))

    def search(self, term, page=1):
        """
        Search for people.
        :param term:
        :param page:
        :return:
        """
        return self._get_obj(self._call(self._urls['search_people'], 'query=' + quote(term) + '&page=' + str(page)))
