from tmdbv3api import TMDb, Collection

tmdb = TMDb()

tmdb.api_key = ""
tmdb.language = "en"

collection = Collection()

# Get collection details

details = collection.details(10)
print(details.id)
print(details.name)
print(details.overview)
print(details.poster_path)
for part in details.parts:
    print(part["id"])
    print(part["title"])

# Get collection images 
# If tmdb.language is 'en-US' will not work. Set tmdb.language to 'en'

images = collection.images(10)
print(images.id)
for image in images.backdrops:
    print(image["file_path"])
    print(image["height"])
    print(image["width"])
for image in images.posters:
    print(image["file_path"])
    print(image["height"])
    print(image["width"])

# Get collection translations
    
translations = collection.translations(10)
for translation in translations:
    print(translation.iso_3166_1)
    print(translation.iso_639_1)
    print(translation.name)
    print(translation.english_name)
    print(translation.data["title"])
    print(translation.data["overview"])
    print(translation.data["homepage"])