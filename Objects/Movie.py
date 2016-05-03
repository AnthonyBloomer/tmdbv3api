import json


class Movie:
    movie_data = []

    def __init__(self, movie_data):
        self.movie_data = movie_data

    def id(self):
        return self.movie_data['id']

    def adult(self):
        return self.movie_data['adult']

    def title(self):
        return self.movie_data['title']

    def overview(self):
        return self.movie_data['overview']

    def poster(self):
        return self.movie_data['poster_path']

    def backdrop_path(self):
        return self.movie_data['backdrop_path']

    def vote_average(self):
        return self.movie_data['vote_average']

    def vote_count(self):
        return self.movie_data['vote_count']

    def popularity(self):
        return self.movie_data['popularity']

    def release_date(self):
        return self.movie_data['release_date']

    def original_language(self):
        return self.movie_data['original_language']

    def original_title(self):
        return self.movie_data['original_title']
        
    def revenue(self):
        return self.movie_data['revenue']

    def belongs_to_collection(self):
        return self.movie_data['belongs_to_collection']

    def json(self):
        return json.dumps(self.movie_data)
