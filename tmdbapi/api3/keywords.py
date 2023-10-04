"""API v3 keywords category

"""

from tmdbapi._core import Tmdb
from tmdbapi.exceptions import ServiceDeprecationWarning

_KEYWORDS_V3 = {
    "keyword-details": {
        "method": "get",
        "params": [{"in": "path", "name": "keyword_id"}],
        "url": "/{keyword_id}",
    },
    "keyword-movies": {
        "method": "get",
        "params": [
            {"in": "path", "name": "keyword_id"},
            {"in": "query", "name": "include_adult"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
        ],
        "url": "/{keyword_id}/movies",
    },
}


class _Keywords(Tmdb):
    def __init__(self, info_var):
        super().__init__()
        self.category_path = "/keyword"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url=url,
        )


def details(keyword_id: int) -> dict:
    keywords = _Keywords(_KEYWORDS_V3)
    keywords.reset()
    keywords.use("keyword-details")
    keywords.load_path_arg(keyword_id=keyword_id)
    return keywords.request()


def movies(keyword_id: int, include_adult=False, language: str = None, page=1) -> dict:
    ServiceDeprecationWarning(
        "keywords.movies method is deprecated, you should use discover.movie instead."
    )
    keywords = _Keywords(_KEYWORDS_V3)
    keywords.reset()
    keywords.use("keyword-movies")
    keywords.load_path_arg(keyword_id=keyword_id)
    keywords.language(language)
    keywords.load_query(include_adult=include_adult, page=page)
    return keywords.request()
