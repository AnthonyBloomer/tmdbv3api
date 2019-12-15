import os

from tmdbv3api.as_obj import AsObj
from tmdbv3api.tmdb import TMDb


class Account(TMDb):
    _urls = {
        'details': '/account'
    }

    def details(self):
        return AsObj(**self._call(self._urls['details'], 'session_id=%s' % os.environ.get('TMDB_SESSION_ID')))
