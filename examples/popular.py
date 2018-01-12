from tmdbv3api import TMDb

tmdb = TMDb()

tmdb.api_key = ''

popular = tmdb.popular()

for p in popular:
    print p.title
    print p.overview
