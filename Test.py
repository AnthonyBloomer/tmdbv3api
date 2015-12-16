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
    print movie.get_vote_average()

top_rated = tmdb.top_rated(page=2)
max = 0

while tmdb.current_page < tmdb.total_pages and max != 5:
    search = tmdb.top_rated(page=tmdb.current_page + 1)
    for movie in search:
        print movie.get_id()
        print movie.get_title()
        print movie.get_overview()
        print movie.get_poster()
        print movie.get_vote_average()

    max += 1
