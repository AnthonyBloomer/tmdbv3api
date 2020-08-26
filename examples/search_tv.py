from tmdbv3api import TMDb, TV

tmdb = TMDb()

tmdb.api_key = ""

tv = TV()

show = tv.search("Breaking Bad")

for result in show:
    print(result.name)
    print(result.overview)
