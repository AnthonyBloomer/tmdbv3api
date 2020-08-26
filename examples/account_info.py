from tmdbv3api import Account
from tmdbv3api import Authentication
from tmdbv3api import TMDb, Movie

USERNAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"

tmdb = TMDb()
tmdb.api_key = "YOUR_API_KEY"

auth = Authentication(username=USERNAME, password=PASSWORD)

account = Account()
details = account.details()

print(
    "You are logged in as %s. Your account ID is %s." % (details.username, details.id)
)
print("This session expires at: %s" % auth.expires_at)

movie = Movie()

s = movie.search("Gangs of New York")
first_result = s[0]
recommendations = movie.recommendations(first_result.id)

for recommendation in recommendations:
    print(
        "Adding %s (%s) to watchlist."
        % (recommendation.title, recommendation.release_date)
    )

    w = account.add_to_watchlist(details.id, recommendation.id, "movie")

    print(w)
