import json


class TVShow:
    tvdata = []

    def __init__(self, movie_data):
        self.tvdata = movie_data

    def get_id(self):
        return self.tvdata['id']

    def get_name(self):
        return self.tvdata['name']

    def get_overview(self):
        return self.tvdata['overview']

    def get_first_air_date(self):
        return self.tvdata['first_air_date']

    def get_last_air_date(self):
        return self.tvdata['last_air_date']

    def get_number_of_episodes(self):
        return self.tvdata['number_of_episodes']

    def get_number_of_seasons(self):
        return self.tvdata['number_of_seasons']

    def get_poster(self):
        return self.tvdata['poster_path']

    def get_backdrop_path(self):
        return self.tvdata['backdrop_path']

    def get_vote_average(self):
        return self.tvdata['vote_average']

    def get_vote_count(self):
        return self.tvdata['vote_count']

    def get_popularity(self):
        return self.tvdata['popularity']

    def get_release_date(self):
        return self.tvdata['release_date']

    def get_original_language(self):
        return self.tvdata['original_language']

    def get_original_name(self):
        return self.tvdata['original_name']

    def get_json(self):
        return json.dumps(self.tvdata)
