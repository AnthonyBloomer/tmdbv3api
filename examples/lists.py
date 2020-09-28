import random

from tmdbv3api import TMDb, List

tmdb = TMDb()
tmdb.api_key = ""

lists = List()
the_list = lists.details(3673)

random_movie = random.choice(the_list)

print("Title: %s (%s)" % (random_movie.title, random_movie.release_date))
print("Rating: %s" % random_movie.vote_average)
print("Overview: %s" % random_movie.overview)
