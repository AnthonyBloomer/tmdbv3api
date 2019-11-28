from tmdbv3api.as_obj import AsObj
from tmdbv3api.tmdb import TMDb

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote


class Episode(TMDb):
    _urls = {
        'details': '/tv/%s/season/%s/episode/%s',
    }

    def details(self, tv_id, season_num, episode_num, append_to_response="trailers,images,casts,translations"):
        return AsObj(
            **self._call(self._urls['details'] % (str(tv_id), str(season_num), str(episode_num)),
                         "append_to_response=%s" % append_to_response))
