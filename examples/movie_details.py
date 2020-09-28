from tmdbv3api import TMDb, Movie

tmdb = TMDb()
tmdb.api_key = ""

movie = Movie()

m = movie.details(111)

print(m.title)
print(m.overview)
print(m.popularity)
