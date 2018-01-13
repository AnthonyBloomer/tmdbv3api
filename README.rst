tmdbv3api
=========

|Build Status| |codecov|

A lightweight Python library for The Movie Database (TMDb) API. This
library allows you to easily interact with the TMDb API and retrieve data on
movies, TV shows and actors.

Register an account: https://www.themoviedb.org/account/signup

Check out the API documentation: https://docs.themoviedb.apiary.io

Install
~~~~~~~

tmdbv3api is available on the Python Package Index (PyPI) at
https://pypi.python.org/pypi/tmdbv3api

You can install tmdbv3api using pip.

::

    $ pip install tmdbv3api

Usage
~~~~~

The first step is to initialize a TMDb object and set your API Key.

.. code:: python

    from tmdbv3api import TMDb
    tmdb = TMDb()
    tmdb.api_key = 'YOUR_API_KEY'

Alternatively, you can export your API key as an environment variable.

.. code:: bash

    $ export api_key='YOUR_API_KEY'

Then to communicate with TMDb, create an instance of one of the objects
and call that instances methods. For example, to retrieve movie
recommendations for a given movie id:

.. code:: python

    from tmdbv3api import Movie

    movie = Movie()

    recommendations = movie.recommendations(movie_id=111)

    for recommendation in recommendations:
        print(recommendation.title)
        print(recommendation.overview)

Examples
~~~~~~~~

Get the list of popular movies on The Movie Database. This list
refreshes every day.

.. code:: python


    movie = Movie()
    popular = movie.popular()

    for p in popular:
        print(p.id)
        print(p.title)
        print(p.overview)
        print(p.poster_path)
                

Get the primary information about a movie.

.. code:: python

    m = movie.details(343611)

    print(m.title)
    print(m.overview)
    print(m.popularity)

Search for movies by title.

.. code:: python

    search = movie.search('Mad Max')

    for res in search:
        print(res.id)
        print(res.title)
        print(res.overview)
        print(res.poster_path)
        print(res.vote_average)

Get the similar movies for a specific movie id.

.. code:: python

    similar = movie.similar(777)

    for result in similar:
        print(result.title)
        print(result.overview)

Search for TV shows by title.

.. code:: python

    tv = TV()
    show = tv.search('Breaking Bad')

    for result in show:
        print(result.name)
        print(result.overview)

Get the similar TV shows for a specific tv id.

.. code:: python

    similar = tv.similar(1396)

    for show in similar:
        print(show.name)
        print(show.overview)

Get the general person information for a specific id.

.. code:: python

    person = Person()
    p = person.details(12)

    print(p.name)
    print(p.biography)

Discover movies by different types of data like average rating, number
of votes, genres and certifications.

.. code:: python


    # What movies are in theatres?

    discover = Discover()
    movie = discover.discover_movies({
        'primary_release_date.gte': '2017-01-20',
        'primary_release_date.lte': '2017-01-25'
    })

    # What are the most popular movies?

    movie = discover.discover_movies({
        'sort_by': 'popularity.desc'
    })

    # What are the most popular kids movies?

    movie = discover.discover_movies({
        'certification_country': 'US',
        'certification.lte': 'G',
        'sort_by': 'popularity.desc'
    })

Discover TV shows by different types of data like average rating, number
of votes, genres, the network they aired on and air dates.

.. code:: python

    # What are the most popular TV shows?

    show = discover.discover_tv_shows({
        'sort_by': 'popularity.desc'
    })

    # What are the best dramas?

    show = discover.discover_tv_shows({
        'with_genres': 18,
        'sort_by': 'vote_average.desc',
        'vote_count.gte': 10
    })

Running Tests
~~~~~~~~~~~~~

You can run the tests via the command line. You must export your TMDb
API key as an environment variable. From the command line run:

.. code:: bash

    $ export api_key='YOUR_API_KEY'

Then run:

.. code:: bash

    $ python -m unittest discover tests/


.. |Build Status| image:: https://travis-ci.org/AnthonyBloomer/tmdbv3api.svg?branch=master
   :target: https://travis-ci.org/AnthonyBloomer/tmdbv3api
.. |codecov| image:: https://codecov.io/gh/AnthonyBloomer/tmdbv3api/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/AnthonyBloomer/tmdbv3api
