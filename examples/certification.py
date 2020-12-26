from tmdbv3api import TMDb, Certification

tmdb = TMDb()

tmdb.api_key = ""

certification = Certification()

# Get movie certifications for USA

movie_certifications = certification.movie_list().certifications

for usa_certification in movie_certifications["US"]:
    print(usa_certification["certification"])
    print(usa_certification["meaning"])


# Get tv show certifications for Spain

tv_certifications = certification.tv_list().certifications

for usa_certification in tv_certifications["ES"]:
    print(usa_certification["certification"])
    print(usa_certification["meaning"])

# Get countries avaiable

for country in movie_certifications:
    print(country)

for country in tv_certifications:
    print(country)