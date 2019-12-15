from tmdbv3api import Account
from tmdbv3api import Authentication
from tmdbv3api import TMDb

USERNAME = None
PASSWORD = None

tmdb = TMDb()
tmdb.api_key = ""

auth = Authentication(username=USERNAME, password=PASSWORD)

account = Account()
details = account.details()

print("You are logged in as %s. Your account ID is %s." % (details.username, details.id))
print("This session expires at: %s" % auth.expires_at)
