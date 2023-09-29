"""API v3 reviews category

"""

from tmdbapi._core import Tmdb


_REVIEWS_V3 = {
    "review-details": {
        "method": "get",
        "params": [{"in": "path", "name": "review_id"}],
        "url": "/{review_id}",
    }
}


class _Review(Tmdb):

    def __init__(self, info_var):
        super().__init__()
        self.base_path = "/review"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url = url,
        )

_review = _Review(_REVIEWS_V3)


def details(review_id: str) -> dict:
    """Retrieve the details of a movie or TV show review.
    """
    _review.reset()
    _review.use("collection-details")
    _review.load_path_arg(review_id=review_id)
    return _review.request()
