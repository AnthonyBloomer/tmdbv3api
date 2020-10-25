from tmdbv3api import TMDb, Search

tmdb = TMDb()

tmdb.api_key = ""

search = Search()

results = search.movies({"query": "Matrix", "year": 1999})

for result in results:
    print(result.title)
    print(result.overview)
