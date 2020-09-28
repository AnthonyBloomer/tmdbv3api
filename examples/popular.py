from tmdbv3api import TMDb, Movie

tmdb = TMDb()

tmdb.api_key = ""

movie = Movie()

popular = movie.popular()

for p in popular:
    print(p.title)
    print(p.overview)
