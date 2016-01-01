# tmdb
Python wrapper for The Movie Database (TMDb) API.

To use this wrapper you will need to obtain an API key from TMDB. Register an account here:
https://www.themoviedb.org/account/signup

Check out the API documentation here: 
https://docs.themoviedb.apiary.io

### Examples

Get a list of popular movies.

```python

from TMDb import TMDb
tmdb = TMDb(apikey="your-api-key", debug=True, language="en")

popular = tmdb.popular()

for movie in popular:
    print movie.get_id()
    print movie.get_title()
    print movie.get_overview()
    print movie.get_poster()
            
```
Search for a movie by name.

```python
search = tmdb.search('Mad Max')

for movie in search:
    print movie.get_id()
    print movie.get_title()
    print movie.get_overview()
    print movie.get_poster()
    print movie.get_vote_average()
```

Get a list of similar movies for a given movie ID.

```python
similar = tmdb.similar(777)

for result in similar:
    print result.get_title()
    print result.get_overview()
```

Search for a TV show by name.

```python
show = tmdb.search_tv('Breaking Bad')

for result in show:
    print result.get_name()
    print result.get_overview()
```

Get a list of similar TV shows for a given TV Show ID.

```python
similar = tmdb.similar_shows(1396)

for show in similar:
    print show.get_name()
    print show.get_overview()
```

Get actor information for a given ID.

```python
person = tmdb.get_person(12)

print person.get_name()
print person.get_biography()
```
