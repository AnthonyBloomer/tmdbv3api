import json


class Movie:
    movie_data = []

    def __init__(self, movie_data):
        self.movie_data = movie_data

    def get_id(self):
        return self.movie_data['id']

    def get_title(self):
        return self.movie_data['title']

    def get_overview(self):
        return self.movie_data['overview']

    def get_poster(self):
        return self.movie_data['poster_path']

    def get_backdrop_path(self):
        return self.movie_data['backdrop_path']

    def get_vote_average(self):
        return self.movie_data['vote_average']

    def get_vote_count(self):
        return self.movie_data['vote_count']

    def get_popularity(self):
        return self.movie_data['popularity']

    def get_release_date(self):
        return self.movie_data['release_date']

    def get_original_language(self):
        return self.movie_data['original_language']

    def get_original_title(self):
        return self.movie_data['original_title']

    def get_json(self):
        return json.dumps(self.movie_data)
