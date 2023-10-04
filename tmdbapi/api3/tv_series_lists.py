"""API v3 tv series lists category

"""

from tmdbapi._core import Tmdb

_TV_SERIES_LISTS_V3 = {
    "tv-series-airing-today-list": {
        "method": "get",
        "params": [
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "timezone"},
        ],
        "url": "/airing_today",
    },
    "tv-series-on-the-air-list": {
        "method": "get",
        "params": [
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "timezone"},
        ],
        "url": "/on_the_air",
    },
    "tv-series-popular-list": {
        "method": "get",
        "params": [
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
        ],
        "url": "/popular",
    },
    "tv-series-top-rated-list": {
        "method": "get",
        "params": [
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
        ],
        "url": "/top_rated",
    },
}


class _TvSeriesLists(Tmdb):
    def __init__(self, info_var):
        super().__init__()
        self.category_path = "/tv"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url=url,
        )


def airing_today(page=1, language: str = None, timezone: str = None) -> dict:
    """Get a list of TV shows airing today.

    timezone:
    Get the list of timezones from configuration.timezones
    """
    tv_series_lists = _TvSeriesLists(_TV_SERIES_LISTS_V3)
    tv_series_lists.reset()
    tv_series_lists.use("tv-series-airing-today-list")
    tv_series_lists.language(language)
    tv_series_lists.load_query(page=page)
    if timezone is not None:
        tv_series_lists.load_query(timezone=timezone)
    return tv_series_lists.request()


def on_the_air(page=1, language: str = None, timezone: str = None) -> dict:
    """Get a list of TV shows that air in the next 7 days.

    timezone:
    Get the list of timezones from configuration.timezones
    """
    tv_series_lists = _TvSeriesLists(_TV_SERIES_LISTS_V3)
    tv_series_lists.reset()
    tv_series_lists.use("tv-series-on-the-air-list")
    tv_series_lists.language(language)
    tv_series_lists.load_query(page=page)
    if timezone is not None:
        tv_series_lists.load_query(timezone=timezone)
    return tv_series_lists.request()


def popular(page=1, language: str = None) -> dict:
    """Get a list of TV shows ordered by popularity."""
    tv_series_lists = _TvSeriesLists(_TV_SERIES_LISTS_V3)
    tv_series_lists.reset()
    tv_series_lists.use("tv-series-popular-list")
    tv_series_lists.language(language)
    tv_series_lists.load_query(page=page)
    return tv_series_lists.request()


def top_rated(page=1, language: str = None) -> dict:
    tv_series_lists = _TvSeriesLists(_TV_SERIES_LISTS_V3)
    tv_series_lists.reset()
    tv_series_lists.use("tv-series-top-rated-list")
    tv_series_lists.language(language)
    tv_series_lists.load_query(page=page)
    return tv_series_lists.request()
