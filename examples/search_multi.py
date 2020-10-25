from tmdbv3api import TMDb, Search

tmdb = TMDb()

tmdb.api_key = ""

search = Search()

results = search.multi({"query": "Will", "page": 1})

for result in results:
    print(result.media_type)
