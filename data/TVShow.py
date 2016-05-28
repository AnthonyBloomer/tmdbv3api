import json


class TVShow:
    tvdata = []

    def __init__(self, tvdata):
        self.tvdata = tvdata

    def id(self):
        return self.tvdata['id']

    def name(self):
        return self.tvdata['name']

    def overview(self):
        return self.tvdata['overview']

    def first_air_date(self):
        return self.tvdata['first_air_date']

    def last_air_date(self):
        return self.tvdata['last_air_date']

    def number_of_episodes(self):
        return self.tvdata['number_of_episodes']

    def number_of_seasons(self):
        return self.tvdata['number_of_seasons']

    def poster(self):
        return self.tvdata['poster_path']

    def backdrop_path(self):
        return self.tvdata['backdrop_path']

    def vote_average(self):
        return self.tvdata['vote_average']

    def vote_count(self):
        return self.tvdata['vote_count']

    def popularity(self):
        return self.tvdata['popularity']

    def release_date(self):
        return self.tvdata['release_date']

    def original_language(self):
        return self.tvdata['original_language']

    def original_name(self):
        return self.tvdata['original_name']

    def status(self):
        return self.tvdata['status']

    def type(self):
        return self.tvdata['type']

    def json(self):
        return json.dumps(self.tvdata)
