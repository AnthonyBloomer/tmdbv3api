from tmdbv3api import TMDb, Genre

tmdb = TMDb()

tmdb.api_key = ""
tmdb.debug = True

genre = Genre()

genres = genre.movie_list()

for g in genres:
    print(g.id)
    print(g.name)
