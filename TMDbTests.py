import unittest
from TMDb import TMDb


class TMDbTests(unittest.TestCase):
    def setUp(self):
        self.api = TMDb(api_key='', debug=False, lang='en')

    def test_get_movie(self):
        movie = self.api.get_movie(111)
        print movie.title()

    def test_get_latest_movie(self):
        movie = self.api.get_latest_movie()
        print movie.title()

    def test_now_playing(self):
        movies = self.api.now_playing()
        for now_playing in movies:
            print now_playing.title()

    def test_top_rated(self):
        movies = self.api.top_rated()
        for top_rated in movies:
            print top_rated.title()
        self.assertIsNotNone(movies)

    def test_upcoming(self):
        upcoming = self.api.upcoming()
        for movie in upcoming:
            print movie.title()
        self.assertIsNotNone(upcoming)

    def test_popular(self):
        popular = self.api.popular()
        for movie in popular:
            print movie.title()
        self.assertIsNotNone(popular)

    def test_search(self):
        search = self.api.search('Breaking Bad')
        self.assertIsNotNone(search)

    def test_similar(self):
        similar = self.api.similar(111)
        self.assertIsNotNone(similar)

    def test_get_tv_show(self):
        show = self.api.get_tv_show(77)
        self.assertIsNotNone(show)

    def test_get_latest_tv_show(self):
        latest = self.api.get_latest_tv_show()
        self.assertIsNotNone(latest)

    def test_search_tv(self):
        search_tv = self.api.search_tv('Breaking Bad')
        self.assertIsNotNone(search_tv)

    def test_similar_shows(self):
        similar = self.api.similar_shows(1396)
        self.assertIsNotNone(similar)

    def test_popular_shows(self):
        popular = self.api.popular_shows()
        self.assertIsNotNone(popular)

    def test_top_rated_shows(self):
        top_rated = self.api.top_rated_shows()
        self.assertIsNotNone(top_rated)

    def test_get_person(self):
        person = self.api.get_person(2)
        self.assertIsNotNone(person)

    def test_search_person(self):
        search = self.api.search_person('Al Pacino')
        for result in search:
            print result.name()
        self.assertIsNotNone(search)


if __name__ == 'main':
    unittest.main()
