from TMDb import TMDb

tmdb = TMDb(apikey="", debug=True)

print tmdb.config

print tmdb.get_image_url()

popular = tmdb.popular()

for movie in popular:
    print movie.get_id()
    print movie.get_title()
    print movie.get_overview()
    print movie.get_poster()

search = tmdb.search('Mad Max')

for movie in search:
    print movie.get_id()
    print movie.get_title()
    print movie.get_overview()
    print movie.get_poster()
