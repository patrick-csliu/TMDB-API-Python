"""API v3 find category

"""

from tmdbapi._core import Tmdb


_FIND_V3 = {
    "find-by-id": {
        "method": "get",
        "params": [
            {"in": "path", "name": "external_id"},
            {"in": "query", "name": "external_source"},
            {"in": "query", "name": "language"},
        ],
        "url": "/{external_id}",
    }
}


class _Find(Tmdb):

    def __init__(self, info_var):
        super().__init__()
        self.base_path = "/find"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url = url,
        )

_find = _Find(_FIND_V3)


def find(external_id: str, external_source: str,
         language: str = None) -> dict:
    """Find data by external ID's.
    """
    _find.reset()
    _find.use("find-by-id")
    _find.load_path_arg(external_id=external_id)
    _find.language(language)
    _find.load_query(external_source=external_source)
    return _find.request()
