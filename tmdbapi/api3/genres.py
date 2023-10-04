"""API v3 genres category

"""

from tmdbapi._core import Tmdb

_GENRES_V3 = {
    "genre-movie-list": {
        "method": "get",
        "params": [{"in": "query", "name": "language"}],
        "url": "/movie/list",
    },
    "genre-tv-list": {
        "method": "get",
        "params": [{"in": "query", "name": "language"}],
        "url": "/tv/list",
    },
}


class _Genres(Tmdb):
    def __init__(self, info_var):
        super().__init__()
        self.category_path = "/genre"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url=url,
        )


def movie_list(language: str = None) -> dict:
    """Get the list of official genres for movies."""
    genres = _Genres(_GENRES_V3)
    genres.reset()
    genres.use("genre-movie-list")
    genres.language(language)
    return genres.request()


def tv_list(language: str = None) -> dict:
    """Get the list of official genres for TV shows."""
    genres = _Genres(_GENRES_V3)
    genres.reset()
    genres.use("genre-tv-list")
    genres.language(language)
    return genres.request()
