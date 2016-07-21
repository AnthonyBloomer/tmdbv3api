from tmdbv3api import TMDb
tmdb = TMDb(api_key="e1076b74406e0a7d0efb5318f1b662d0", debug=False, lang="en")

popular = tmdb.popular()

for movie in popular:
    print movie.id()
    print movie.title()
    print movie.overview()
    print movie.poster()
