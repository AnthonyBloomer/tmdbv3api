# Simple program that takes a movie name as an argument and finds movie recommendations for the user.

from tmdbv3api import TMDb, Movie
from argparse import ArgumentParser

tmdb = TMDb()
tmdb.api_key = ''

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('movie')
    parser.add_argument('--limit', nargs='?', default=1)
    args = parser.parse_args()
    movie = Movie()
    search = movie.search(args.movie)
    first_result = search[0]
    recommendations = movie.recommendations(first_result.id)
    count = 0
    for recommendation in recommendations:
        if (count == args.limit):
            break
        print("%s (%s)" % (recommendation.title, recommendation.release_date))
        count += 1
    
    
    
