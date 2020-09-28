from tmdbv3api import TMDb, Configuration

tmdb = TMDb()
tmdb.api_key = ""

config = Configuration()
info = config.info()

poster_sizes = info.images["poster_sizes"]
print(poster_sizes)

secure_base_url = info.images["secure_base_url"]
print(secure_base_url)
