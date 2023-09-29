"""API v3 credits category

"""

from tmdbapi._core import Tmdb


_CREDITS_V3 = {
    "credit-details": {
        "method": "get",
        "params": [{"in": "path", "name": "credit_id"}],
        "url": "/{credit_id}",
    }
}


class _Credits(Tmdb):

    def __init__(self, info_var):
        super().__init__()
        self.base_path = "/credit"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url = url,
        )

_credits = _Credits(_CREDITS_V3)


def details(credit_id: str) -> dict:
    """Get a movie or TV credit details by ID.
    """
    _credits.reset()
    _credits.use("credit-details")
    _credits.load_path_arg(credit_id=credit_id)
    return _credits.request()
