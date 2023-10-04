"""API v3 watch providers category

"""

from tmdbapi._core import Tmdb

_WATCH_PROVIDERS_V3 = {
    "watch-provider-tv-list": {
        "method": "get",
        "params": [
            {"in": "query", "name": "language"},
            {"in": "query", "name": "watch_region"},
        ],
        "url": "/tv",
    },
    "watch-providers-available-regions": {
        "method": "get",
        "params": [{"in": "query", "name": "language"}],
        "url": "/regions",
    },
    "watch-providers-movie-list": {
        "method": "get",
        "params": [
            {"in": "query", "name": "language"},
            {"in": "query", "name": "watch_region"},
        ],
        "url": "/movie",
    },
}


class _WatchProviders(Tmdb):
    def __init__(self, info_var):
        super().__init__()
        self.category_path = "/watch/providers"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url=url,
        )


def available_regions(language: str = None) -> dict:
    """Get the list of the countries we have watch provider
    (OTT/streaming) data for.
    """
    watch_providers = _WatchProviders(_WATCH_PROVIDERS_V3)
    watch_providers.reset()
    watch_providers.use("watch-providers-available-regions")
    watch_providers.language(language)
    return watch_providers.request()


def movie_providers(watch_region: str = None, language: str = None) -> dict:
    """Get the list of streaming providers we have for movies."""
    watch_providers = _WatchProviders(_WATCH_PROVIDERS_V3)
    watch_providers.reset()
    watch_providers.use("watch-providers-movie-list")
    watch_providers.language(language)
    if watch_region is not None:
        watch_providers.load_query(watch_region=watch_region)
    return watch_providers.request()


def tv_providers(watch_region: str = None, language: str = None) -> dict:
    """Get the list of streaming providers we have for TV shows."""
    watch_providers = _WatchProviders(_WATCH_PROVIDERS_V3)
    watch_providers.reset()
    watch_providers.use("watch-provider-tv-list")
    watch_providers.language(language)
    if watch_region is not None:
        watch_providers.load_query(watch_region=watch_region)
    return watch_providers.request()
