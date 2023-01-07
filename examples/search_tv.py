from tmdbv3api import TMDb, TV

tmdb = TMDb()

tmdb.api_key = ""

search = Search()

show = search.tv_shows("Breaking Bad")

for result in show:
    print(result.name)
    print(result.overview)
