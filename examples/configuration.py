from tmdbv3api import TMDb, Configuration

tmdb = TMDb()
tmdb.api_key = ""

configuration = Configuration()

info = configuration.info()

print('Change keys: ' + ', '.join(info.change_keys))
print('Base url: ' + info.images["base_url"])
print('Secure base url: ' + info.images["secure_base_url"])
print('Backdrop sizes: ' + ', '.join(info.images["backdrop_sizes"]))
print('Logo sizes: ' + ', '.join(info.images["logo_sizes"]))
print('Poster sizes: ' + ', '.join(info.images["poster_sizes"]))
print('Profile sizes: ' + ', '.join(info.images["profile_sizes"]))
print('Still sizes: ' + ', '.join(info.images["still_sizes"]))

countries = configuration.countries()

for country in countries:
    print('English name: ' + country['english_name'])
    print('iso_3166_1: ' + country['iso_3166_1'])

jobs = configuration.jobs()

for job in jobs:
    print(job['department'] + ': ' + ', '.join(job['jobs']))

languages = configuration.languages()

for language in languages:
    print('English name: ' + language['english_name'])
    print('Name: ' + language['name'])
    print('iso_639_1: ' + language['iso_639_1'])

primary_translations = configuration.primary_translations()

print('Primary translations: ' + ', '.join(primary_translations))

timezones = configuration.timezones()

for timezone in timezones:
    print(timezone['iso_3166_1'] + ': ' + ', '.join(timezone['zones']))
