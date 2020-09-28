from tmdbv3api import TMDb, Discover

tmdb = TMDb()

tmdb.api_key = ""

discover = Discover()

# What are the most popular TV shows?

show = discover.discover_tv_shows({"sort_by": "popularity.desc"})

for p in show:
    print(p.name)
    print(p.overview)
    print("")
