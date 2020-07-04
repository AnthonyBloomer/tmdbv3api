# Simple program that takes a movie name as an argument and finds movie recommendations for the user.

from tmdbv3api import TMDb, Movie
from argparse import ArgumentParser

tmdb = TMDb()
tmdb.api_key = ""


def search(query, limit):
    movie = Movie()
    s = movie.search(query)
    first_result = s[0]
    recommendations = movie.recommendations(first_result.id)
    recommendations = (
        recommendations[: int(limit)] if recommendations >= limit else recommendations
    )
    for recommendation in recommendations:
        print("%s (%s)" % (recommendation.title, recommendation.release_date))


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("movie")
    parser.add_argument("--limit", nargs="?", default=1)
    args = parser.parse_args()
    search(args.movie, args.limit)
