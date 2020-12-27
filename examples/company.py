from tmdbv3api import TMDb, Company

tmdb = TMDb()

tmdb.api_key = ""

company = Company()

# Company details

details = company.details(1)
print(details.description)
print(details.headquarters)
print(details.homepage)
print(details.id)
print(details.logo_path)
print(details.name)
print(details.origin_country)
print(details.parent_company)

# Company alternative names

alternative_names = company.alternative_names(1)
for alternative_name in alternative_names:
    print(alternative_name.name)
    print(alternative_name.type)

# Company images

images = company.images(1)
for image in images:
    print(image.aspect_ratio)
    print(image.file_path)
    print(image.height)
    print(image.id)
    print(image.file_type)
    print(image.vote_average)
    print(image.vote_count)
    print(image.width)

# Company movies

movies = company.movies(1)
for movie in movies:
    print(movie.id)
    print(movie.title)
    print(movie.overview)
