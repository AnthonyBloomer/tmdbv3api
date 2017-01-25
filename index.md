# tmdbv3api
Python wrapper for The Movie Database (TMDb) API.

To use this wrapper you will need to get an API key from TMDb.

Register an account:
https://www.themoviedb.org/account/signup

Check out the API documentation: 
https://docs.themoviedb.apiary.io

### Install

```
pip install tmdbv3api
```

### Examples

Get the list of popular movies on The Movie Database. This list refreshes every day.

```python

from tmdbv3api import TMDb
tmdb = TMDb(api_key="your_api_key", debug=False, lang="en")

popular = tmdb.popular()

for movie in popular:
    print movie.id
    print movie.title
    print movie.overview
    print movie.poster_path
            
```

Get the primary information about a movie.

```python
movie = tmdb.get_movie('343611')
print movie.title
print movie.overview
print movie.popularity
```

Search for movies by title.

```python
search = tmdb.search('Mad Max')

for movie in search:
    print movie.id
    print movie.title
    print movie.overview
    print movie.poster_path
    print movie.vote_average
```

Get the similar movies for a specific movie id.

```python
similar = tmdb.similar(777)

for result in similar:
    print result.title
    print result.overview
```

Search for TV shows by title.

```python
show = tmdb.search_tv('Breaking Bad')

for result in show:
    print result.name
    print result.overview
```

Get the similar TV shows for a specific tv id.

```python
similar = tmdb.similar_shows(1396)

for show in similar:
    print show.name
    print show.overview
```

Get the general person information for a specific id.

```python
person = tmdb.get_person(12)

print person.name
print person.biography
```

Discover movies by different types of data like average rating, number of votes, genres and certifications. 

```python

# What movies are in theatres?

movie = tmdb.discover_movies({
    'primary_release_date.gte': '2017-01-20',
    'primary_release_date.lte': '2017-01-25'
})

# What are the most popular movies?

movie = tmdb.discover_movies({
    'sort_by': 'popularity.desc'
})

# What are the most popular kids movies?

movie = tmdb.discover_movies({
    'certification_country': 'US',
    'certification.lte': 'G',
    'sort_by': 'popularity.desc'
})

```

Discover TV shows by different types of data like average rating, number of votes, genres, the network they aired on and air dates.

```python
# What are the most popular TV shows?

show = tmdb.discover_tv_shows({
    'sort_by': 'popularity.desc'
})

# What are the best dramas?

show = tmdb.discover_tv_shows({
    'with_genres': 18,
    'sort_by': 'vote_average.desc',
    'vote_count.gte': 10
})

```

### Supported Methods

#### Movies
- **/movie/latest** 
- **/movie/now_playing**
- **/movie/top_rated**
- **/movie/upcoming**
- **/movie/id**
- **/movie/id/similar**
- **/movie/id/recommendations**
- **/movie/id/videos**
- **/movie/id/reviews**
- **/movie/id/lists**


#### TV

- **/tv/id**
- **/tv/latest**
- **/tv/id/similar** 
- **/tv/top_rated**
- **/tv/popular**

#### People

- **/person/id**

#### Search

- **/search/movie**
- **/search/tv**
- **/search/person**

#### Discover

- **/discover/movie**
- **/discover/tv**
