class Endpoint(object):
    BASE = "http://api.themoviedb.org/3/"
    CONFIGURATION = "configuration"

    MOVIE = "movie/"
    MOVIE_REVIEWS = "movie/%s/reviews"
    MOVIE_LISTS = "movie/%s/lists"
    MOVIE_VIDEOS = 'movie/%s/videos'
    MOVIE_RECOMMENDATIONS = 'movie/%s/recommendations'
    MOVIE_LATEST = 'movie/latest'
    MOVIE_SIMILAR = 'movie/%s/similar'

    NOW_PLAYING = 'movie/now_playing'
    TOP_RATED = 'movie/top_rated'
    UPCOMING = 'movie/upcoming'
    POPULAR = 'movie/popular'

    DISCOVER_MOVIES = 'discover/movie/'
    DISCOVER_TV = 'discover/tv/'

    TV_LATEST = 'tv/latest'
    TV_SHOW = 'tv/%s'
    TV_TOP_RATED = 'tv/top_rated'
    TV_POPULAR = 'tv/popular'
    TV_SIMILAR = 'tv/%s/similar'

    SEARCH_MOVIE = "search/movie"
    SEARCH_TV = 'search/tv'
    SEARCH_PERSON = 'search/person'

    PERSON = 'person/%s'