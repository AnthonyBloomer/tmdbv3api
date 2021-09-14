from tmdbv3api.tmdb import TMDb


class Episode(TMDb):
    _urls = {
        "details": "/tv/%s/season/%s/episode/%s",
        "external_ids": "/tv/%s/season/%s/episode/%s/external_ids",
    }

    def details(self, tv_id, season_num, episode_num, append_to_response="trailers,images,casts,translations"):
        """
        Get the TV episode details by id.
        :param tv_id: int
        :param season_num: int
        :param episode_num: int
        :param append_to_response: str
        :return:
        """
        return self._request_obj(
            self._urls["details"] % (tv_id, season_num, episode_num),
            params="append_to_response=%s" % append_to_response
        )

    def external_ids(self, tv_id, season_num, episode_num):
        """
        Get the external ids for a TV episode.
        :param tv_id: int
        :param season_num: int
        :param episode_num: int
        :return:
        """
        return self._request_obj(self._urls["external_ids"] % (tv_id, season_num, episode_num))
