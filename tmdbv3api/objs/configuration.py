from tmdbv3api.tmdb import TMDb
from tmdbv3api.as_obj import AsObj


class Configuration(TMDb):
    _urls = {
        'info': '/configuration'
    }

    def info(self):
        """
        Get the system wide configuration info.
        """
        return AsObj(**self._call(self._urls['info'], ''))
