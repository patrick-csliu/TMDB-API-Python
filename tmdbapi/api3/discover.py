"""API v3 discover category

"""
from tmdbapi._core import Tmdb

_DISCOVER_V3 = {
    "discover-movie": {
        "method": "get",
        "params": [
            {"in": "query", "name": "certification"},
            {"in": "query", "name": "certification.gte"},
            {"in": "query", "name": "certification.lte"},
            {"in": "query", "name": "certification_country"},
            {"in": "query", "name": "include_adult"},
            {"in": "query", "name": "include_video"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "primary_release_year"},
            {"in": "query", "name": "primary_release_date.gte"},
            {"in": "query", "name": "primary_release_date.lte"},
            {"in": "query", "name": "region"},
            {"in": "query", "name": "release_date.gte"},
            {"in": "query", "name": "release_date.lte"},
            {"in": "query", "name": "sort_by"},
            {"in": "query", "name": "vote_average.gte"},
            {"in": "query", "name": "vote_average.lte"},
            {"in": "query", "name": "vote_count.gte"},
            {"in": "query", "name": "vote_count.lte"},
            {"in": "query", "name": "watch_region"},
            {"in": "query", "name": "with_cast"},
            {"in": "query", "name": "with_companies"},
            {"in": "query", "name": "with_crew"},
            {"in": "query", "name": "with_genres"},
            {"in": "query", "name": "with_keywords"},
            {"in": "query", "name": "with_origin_country"},
            {"in": "query", "name": "with_original_language"},
            {"in": "query", "name": "with_people"},
            {"in": "query", "name": "with_release_type"},
            {"in": "query", "name": "with_runtime.gte"},
            {"in": "query", "name": "with_runtime.lte"},
            {"in": "query", "name": "with_watch_monetization_types"},
            {"in": "query", "name": "with_watch_providers"},
            {"in": "query", "name": "without_companies"},
            {"in": "query", "name": "without_genres"},
            {"in": "query", "name": "without_keywords"},
            {"in": "query", "name": "without_watch_providers"},
            {"in": "query", "name": "year"},
        ],
        "url": "/movie",
    },
    "discover-tv": {
        "method": "get",
        "params": [
            {"in": "query", "name": "air_date.gte"},
            {"in": "query", "name": "air_date.lte"},
            {"in": "query", "name": "first_air_date_year"},
            {"in": "query", "name": "first_air_date.gte"},
            {"in": "query", "name": "first_air_date.lte"},
            {"in": "query", "name": "include_adult"},
            {"in": "query", "name": "include_null_first_air_dates"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "screened_theatrically"},
            {"in": "query", "name": "sort_by"},
            {"in": "query", "name": "timezone"},
            {"in": "query", "name": "vote_average.gte"},
            {"in": "query", "name": "vote_average.lte"},
            {"in": "query", "name": "vote_count.gte"},
            {"in": "query", "name": "vote_count.lte"},
            {"in": "query", "name": "watch_region"},
            {"in": "query", "name": "with_companies"},
            {"in": "query", "name": "with_genres"},
            {"in": "query", "name": "with_keywords"},
            {"in": "query", "name": "with_networks"},
            {"in": "query", "name": "with_origin_country"},
            {"in": "query", "name": "with_original_language"},
            {"in": "query", "name": "with_runtime.gte"},
            {"in": "query", "name": "with_runtime.lte"},
            {"in": "query", "name": "with_status"},
            {"in": "query", "name": "with_watch_monetization_types"},
            {"in": "query", "name": "with_watch_providers"},
            {"in": "query", "name": "without_companies"},
            {"in": "query", "name": "without_genres"},
            {"in": "query", "name": "without_keywords"},
            {"in": "query", "name": "without_watch_providers"},
            {"in": "query", "name": "with_type"},
        ],
        "url": "/tv",
    },
}


class _Discover(Tmdb):
    def __init__(self, info_var):
        super().__init__()
        self.category_path = "/discover"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url=url,
        )


def movies(params: dict = {}, **kwargs) -> dict:
    """Find movies using over 30 filters and sort options."""
    discover = _Discover(_DISCOVER_V3)
    discover.reset()
    discover.use("discover-movie")
    params.update(kwargs)
    if not discover.check_params(params):
        raise KeyError("The keyword in params is invalid")
    discover.load_query(params)
    discover.language(params.get("language", None))
    discover.region(params.get("region", None))
    return discover.request()


def tv(params: dict = {}, **kwargs) -> dict:
    """Find TV shows using over 30 filters and sort options."""
    discover = _Discover(_DISCOVER_V3)
    discover.reset()
    discover.use("discover-tv")
    params.update(kwargs)
    if not discover.check_params(params):
        raise KeyError("params error")
    discover.load_query(params)
    discover.language(params.get("language", None))
    discover.region(params.get("region", None))
    return discover.request()
