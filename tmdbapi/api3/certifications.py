"""API v3 certification category

"""

from tmdbapi._core import Tmdb

_CERTIFICATION_V3 = {
    "certification-movie-list": {
        "method": "get",
        "params": [],
        "url": "/movie/list",
    },
    "certifications-tv-list": {
        "method": "get",
        "params": [],
        "url": "/tv/list",
    },
}


class _Certification(Tmdb):
    def __init__(self, info_var):
        super().__init__()
        self.category_path = "/certification"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url=url,
        )


def movie_list() -> dict:
    """Get an up to date list of the officially supported movie certifications on TMDB."""
    certification = _Certification(_CERTIFICATION_V3)
    certification.reset()
    certification.use("certification-movie-list")
    return certification.request()


def tv_list() -> dict:
    certification = _Certification(_CERTIFICATION_V3)
    certification.reset()
    certification.use("certifications-tv-list")
    return certification.request()
