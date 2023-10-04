"""API v3 movie lists category

"""

from tmdbapi._core import Tmdb

_MOVIE_LISTS_V3 = {
    "movie-now-playing-list": {
        "method": "get",
        "params": [
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "region"},
        ],
        "url": "/now_playing",
    },
    "movie-popular-list": {
        "method": "get",
        "params": [
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "region"},
        ],
        "url": "/popular",
    },
    "movie-top-rated-list": {
        "method": "get",
        "params": [
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "region"},
        ],
        "url": "/top_rated",
    },
    "movie-upcoming-list": {
        "method": "get",
        "params": [
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "region"},
        ],
        "url": "/upcoming",
    },
}


class _MovieLists(Tmdb):
    def __init__(self, info_var):
        super().__init__()
        self.category_path = "/movie"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url=url,
        )

    def get_list(self, use_name, language, region, page=1) -> dict:
        """Wrap the process for getting list"""
        self.reset()
        self.use(use_name)
        self.language(language)
        self.region(region)
        self.load_query(page=page)
        return self.request()


def now_playing(language: str = None, region: str = None, page=1) -> dict:
    """Get a list of movies that are currently in theatres."""
    movie_lists = _MovieLists(_MOVIE_LISTS_V3)
    return movie_lists.get_list(
        "movie-now-playing-list", language=language, region=region, page=page
    )


def popular(language: str = None, region: str = None, page=1) -> dict:
    """Get a list of movies ordered by popularity."""
    movie_lists = _MovieLists(_MOVIE_LISTS_V3)
    return movie_lists.get_list(
        "movie-popular-list", language=language, region=region, page=page
    )


def top_rated(language: str = None, region: str = None, page=1) -> dict:
    """Get a list of movies ordered by rating."""
    movie_lists = _MovieLists(_MOVIE_LISTS_V3)
    return movie_lists.get_list(
        "movie-top-rated-list", language=language, region=region, page=page
    )


def upcoming(language: str = None, region: str = None, page=1) -> dict:
    """Get a list of movies that are being released soon."""
    movie_lists = _MovieLists(_MOVIE_LISTS_V3)
    return movie_lists.get_list(
        "movie-upcoming-list", language=language, region=region, page=page
    )
