from tmdbv3api.tmdb import TMDb
from tmdbv3api.as_obj import AsObj

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode


class Collection(TMDb):
    _urls = {
        'images': '/collection/%s/images',
        'details': '/collection/%s'
    }

    def images(self, collection_id):
        """
        Get the images for a collection by id.
        :param collection_id:
        :return:
        """
        return AsObj(**self._call(self._urls['images'] % str(collection_id), ''))

    def details(self, collection_id):
        """
        Get collection details by id.
        :param collection_id:
        :return:
        """
        return AsObj(**self._call(self._urls['details'] % str(collection_id), ''))
