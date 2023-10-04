"""API v3 trending category

"""

from tmdbapi._core import Tmdb
from tmdbapi.exceptions import type_checking

_TRENDING_V3 = {
    "trending-all": {
        "method": "get",
        "params": [
            {"in": "path", "name": "time_window"},
            {"in": "query", "name": "language"},
        ],
        "url": "/all/{time_window}",
    },
    "trending-movies": {
        "method": "get",
        "params": [
            {"in": "path", "name": "time_window"},
            {"in": "query", "name": "language"},
        ],
        "url": "/movie/{time_window}",
    },
    "trending-people": {
        "method": "get",
        "params": [
            {"in": "path", "name": "time_window"},
            {"in": "query", "name": "language"},
        ],
        "url": "/person/{time_window}",
    },
    "trending-tv": {
        "method": "get",
        "params": [
            {"in": "path", "name": "time_window"},
            {"in": "query", "name": "language"},
        ],
        "url": "/tv/{time_window}",
    },
}


class _Trending(Tmdb):
    def __init__(self, info_var):
        super().__init__()
        self.category_path = "/trending"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url=url,
        )

    def get(self, use_name, time_window, language) -> dict:
        """Wrap for the same process"""
        self.reset()
        self.use(use_name)
        self.load_path_arg(time_window=time_window)
        self.language(language)
        return self.request()


def all(time_window="day", language: str = None) -> dict:
    """Get the trending movies, TV shows and people.

    time_window: 'day' or 'week'
    """
    trending = _Trending(_TRENDING_V3)
    type_checking("time_window", time_window)
    return trending.get("trending-all", time_window, language)


def movies(time_window="day", language: str = None) -> dict:
    """Get the trending movies on TMDB."""
    trending = _Trending(_TRENDING_V3)
    type_checking("time_window", time_window)
    return trending.get("trending-movies", time_window, language)


def people(time_window="day", language: str = None) -> dict:
    """Get the trending people on TMDB."""
    trending = _Trending(_TRENDING_V3)
    type_checking("time_window", time_window)
    return trending.get("trending-people", time_window, language)


def tv(time_window="day", language: str = None) -> dict:
    """Get the trending TV shows on TMDB."""
    trending = _Trending(_TRENDING_V3)
    type_checking("time_window", time_window)
    return trending.get("trending-tv", time_window, language)
