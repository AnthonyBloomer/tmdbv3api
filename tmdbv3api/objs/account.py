import os

from tmdbv3api.exceptions import TMDbException
from tmdbv3api.tmdb import TMDb


class Account(TMDb):
    _urls = {
        "details": "/account",
        "watchlist": "/account/%s/watchlist",
    }

    @property
    def account_id(self):
        if not os.environ.get("TMDB_ACCOUNT_ID"):
            os.environ["TMDB_ACCOUNT_ID"] = str(self.details()["id"])
        return os.environ.get("TMDB_ACCOUNT_ID")

    def details(self):
        """
        Get your account details.
        :return:
        """
        return self._request_obj(
            self._urls["details"],
            params="session_id=%s" % self.session_id
        )

    def add_to_watchlist(self, media_id, media_type, watchlist=True):
        """
        Add a movie or TV show to your watchlist.
        :param media_id: int
        :param media_type: str
        :param watchlist: bool
        """
        if media_type not in ["tv", "movie"]:
            raise TMDbException("Media Type should be tv or movie.")
        self._request_obj(
            self._urls["watchlist"] % self.account_id,
            "session_id=%s" % self.session_id,
            method="POST",
            json={
                "media_type": media_type,
                "media_id": media_id,
                "watchlist": watchlist,
            }
        )
