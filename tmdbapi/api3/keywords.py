"""API v3 keywords category

"""

from tmdbapi._core import Tmdb


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
        self.base_path = "/keyword"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url = url,
        )

_keywords = _Keywords(_KEYWORDS_V3)


def details(keyword_id: int) -> dict:

    _keywords.reset()
    _keywords.use("keyword-details")
    _keywords.load_path_arg(keyword_id=keyword_id)
    return _keywords.request()


def movies(keyword_id: int, include_adult=False,
           language: str = None, page=1) -> dict:

    _keywords.reset()
    _keywords.use("keyword-movies")
    _keywords.load_path_arg(keyword_id=keyword_id)
    _keywords.language(language)
    _keywords.load_query(include_adult=include_adult, page=page)
    return _keywords.request()
