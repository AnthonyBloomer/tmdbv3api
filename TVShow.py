import json


class TVShow:
    tv_data = []

    def __init__(self, movie_data):
        self.tv_data = movie_data

    def get_id(self):
        return self.tv_data['id']

    def get_name(self):
        return self.tv_data['name']

    def get_overview(self):
        return self.tv_data['overview']

    def get_poster(self):
        return self.tv_data['poster_path']

    def get_vote_average(self):
        return self.tv_data['vote_average']

    def get_vote_count(self):
        return self.tv_data['vote_count']

    def get_popularity(self):
        return self.tv_data['popularity']

    def get_release_date(self):
        return self.tv_data['release_date']

    def get_original_language(self):
        return self.tv_data['original_language']

    def get_original_title(self):
        return self.tv_data['original_title']

    def get_json(self):
        return json.dumps(self.tv_data)
