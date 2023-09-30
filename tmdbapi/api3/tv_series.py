"""API v3 tv series category

"""

from tmdbapi._core import Tmdb
from tmdbapi.exceptions import type_checking


_TV_SERIES_V3 = {
    "tv-series-account-states": {
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "session_id"},
            {"in": "query", "name": "guest_session_id"},
        ],
        "url": "/{series_id}/account_states",
    },
    "tv-series-add-rating": {
        "method": "post",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "guest_session_id"},
            {"in": "query", "name": "session_id"},
            {"in": "body", "name": "RAW_BODY"},
            {"in": "header", "name": "Content-Type"},
        ],
        "url": "/{series_id}/rating",
    },
    "tv-series-aggregate-credits": {
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "language"},
        ],
        "url": "/{series_id}/aggregate_credits",
    },
    "tv-series-alternative-titles": {
        "method": "get",
        "params": [{"in": "path", "name": "series_id"}],
        "url": "/{series_id}/alternative_titles",
    },
    "tv-series-changes": {
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "end_date"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "start_date"},
        ],
        "url": "/{series_id}/changes",
    },
    "tv-series-content-ratings": {
        "method": "get",
        "params": [{"in": "path", "name": "series_id"}],
        "url": "/{series_id}/content_ratings",
    },
    "tv-series-credits": {
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "language"},
        ],
        "url": "/{series_id}/credits",
    },
    "tv-series-delete-rating": {
        "method": "delete",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "header", "name": "Content-Type"},
            {"in": "query", "name": "guest_session_id"},
            {"in": "query", "name": "session_id"},
        ],
        "url": "/{series_id}/rating",
    },
    "tv-series-details": {
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "append_to_response"},
            {"in": "query", "name": "language"},
        ],
        "url": "/{series_id}",
    },
    "tv-series-episode-groups": {
        "method": "get",
        "params": [{"in": "path", "name": "series_id"}],
        "url": "/{series_id}/episode_groups",
    },
    "tv-series-external-ids": {
        "method": "get",
        "params": [{"in": "path", "name": "series_id"}],
        "url": "/{series_id}/external_ids",
    },
    "tv-series-images": {
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "include_image_language"},
            {"in": "query", "name": "language"},
        ],
        "url": "/{series_id}/images",
    },
    "tv-series-keywords": {
        "method": "get",
        "params": [{"in": "path", "name": "series_id"}],
        "url": "/{series_id}/keywords",
    },
    "tv-series-latest-id": {"method": "get", "params": [], "url": "/latest"},
    "tv-series-recommendations": {
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
        ],
        "url": "/{series_id}/recommendations",
    },
    "tv-series-reviews": {
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
        ],
        "url": "/{series_id}/reviews",
    },
    "tv-series-screened-theatrically": {
        "method": "get",
        "params": [{"in": "path", "name": "series_id"}],
        "url": "/{series_id}/screened_theatrically",
    },
    "tv-series-similar": {
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
        ],
        "url": "/{series_id}/similar",
    },
    "tv-series-translations": {
        "method": "get",
        "params": [{"in": "path", "name": "series_id"}],
        "url": "/{series_id}/translations",
    },
    "tv-series-videos": {
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "include_video_language"},
            {"in": "query", "name": "language"},
        ],
        "url": "/{series_id}/videos",
    },
    "tv-series-watch-providers": {
        "method": "get",
        "params": [{"in": "path", "name": "series_id"}],
        "url": "/{series_id}/watch/providers",
    },
}


class _TvSeries(Tmdb):

    def __init__(self, info_var):
        super().__init__()
        self.base_path = "/tv"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url = url,
        )

_tv_series = _TvSeries(_TV_SERIES_V3)


def details(series_id: int,
            append_to_response="videos,trailers,images,credits,translations",
            language: str = None) -> dict:
    """Get the details of a TV show.
    """
    _tv_series.reset()
    _tv_series.use("tv-series-details")
    _tv_series.load_path_arg(series_id=series_id)
    _tv_series.language(language)
    _tv_series.load_query(append_to_response=append_to_response)
    return _tv_series.request()


def account_states(series_id: int, guest_session_id: str = None) -> dict:
    """Get the rating, watchlist and favorite status."""
    _tv_series.reset()
    _tv_series.use("tv-series-account-states")
    _tv_series.load_path_arg(series_id=series_id)
    _tv_series.choose_session_id(guest_session_id)
    return _tv_series.request()


def aggregate_credits(series_id: int, language: str = None) -> dict:
    """Get the aggregate credits (cast and crew) that have been added 
    to a TV show.
    """
    _tv_series.reset()
    _tv_series.use("tv-series-aggregate-credits")
    _tv_series.load_path_arg(series_id=series_id)
    _tv_series.language(language)
    return _tv_series.request()


def alternative_titles(series_id: int) -> dict:
    """Get the alternative titles that have been added to a TV show.
    """
    _tv_series.reset()
    _tv_series.use("tv-series-alternative-titles")
    _tv_series.load_path_arg(series_id=series_id)
    return _tv_series.request()


def changes(series_id: int, start_date="", end_date="", page=1) -> dict:
    """Get the recent changes for a TV show.
    
    `start_date` and `start_date` is lte and gte
    Format: YYYY-MM-DD
    """
    type_checking("date", start_date)
    type_checking("date", end_date)
    _tv_series.reset()
    _tv_series.use("tv-series-changes")
    _tv_series.load_path_arg(series_id=series_id)
    if start_date != "":
        _tv_series.load_query(start_date=start_date)
    if end_date != "":
        _tv_series.load_query(end_date=end_date)
    _tv_series.load_query(page=page)
    return _tv_series.request()


def content_ratings(series_id: int) -> dict:
    """Get the content ratings that have been added to a TV show.
    """
    _tv_series.reset()
    _tv_series.use("tv-series-content-ratings")
    _tv_series.load_path_arg(series_id=series_id)
    return _tv_series.request()


def credits(series_id: int, language: str = None) -> dict:
    """Get the latest season credits of a TV show.
    """
    _tv_series.reset()
    _tv_series.use("tv-series-credits")
    _tv_series.load_path_arg(series_id=series_id)
    _tv_series.language(language)
    return _tv_series.request()


def episode_groups(series_id: int) -> dict:
    """Get the episode groups that have been added to a TV show.
    """
    _tv_series.reset()
    _tv_series.use("tv-series-episode-groups")
    _tv_series.load_path_arg(series_id=series_id)
    return _tv_series.request()


def external_ids(series_id: int) -> dict:
    """Get a list of external IDs that have been added to a TV show.
    """
    _tv_series.reset()
    _tv_series.use("tv-series-external-ids")
    _tv_series.load_path_arg(series_id=series_id)
    return _tv_series.request()


def images(series_id: int,
           language: str = None, include_image_language: str = None) -> dict:
    """Get the images that belong to a TV series.
    
    include_image_language:
    specify a comma separated list of ISO-639-1 values to query, 
    for example: en,null
    """
    _tv_series.reset()
    _tv_series.use("")
    _tv_series.load_path_arg(series_id=series_id)
    _tv_series.language(language)
    if include_image_language is not None:
        _tv_series.load_query(include_image_language=include_image_language)
    return _tv_series.request()


def keywords(series_id: int) -> dict:
    """Get a list of keywords that have been added to a TV show.
    """
    _tv_series.reset()
    _tv_series.use("tv-series-keywords")
    _tv_series.load_path_arg(series_id=series_id)
    return _tv_series.request()


def latest() -> dict:
    """Get the newest TV show ID.
    """
    _tv_series.reset()
    _tv_series.use("tv-series-latest-id")
    return _tv_series.request()


def recommendations(series_id: int, page=1, language: str = None) -> dict:

    _tv_series.reset()
    _tv_series.use("tv-series-recommendations")
    _tv_series.load_path_arg(series_id=series_id)
    _tv_series.language(language)
    _tv_series.load_query(page=page)
    return _tv_series.request()


def reviews(series_id: int, page=1, language: str = None) -> dict:
    """Get the reviews that have been added to a TV show.
    """
    _tv_series.reset()
    _tv_series.use("tv-series-reviews")
    _tv_series.load_path_arg(series_id=series_id)
    _tv_series.language(language)
    _tv_series.load_query(page=page)
    return _tv_series.request()


def screened_theatrically(series_id: int) -> dict:
    """Get the seasons and episodes that have screened theatrically.
    """
    _tv_series.reset()
    _tv_series.use("tv-series-screened-theatrically")
    _tv_series.load_path_arg(series_id=series_id)
    return _tv_series.request()


def similar(series_id: int, page=1, language: str = None) -> dict:
    """Get the similar TV shows.
    """
    _tv_series.reset()
    _tv_series.use("tv-series-similar")
    _tv_series.load_path_arg(series_id=series_id)
    _tv_series.language(language)
    _tv_series.load_query(page=page)
    return _tv_series.request()


def translations(series_id: int) -> dict:
    """Get the translations that have been added to a TV show.
    """
    _tv_series.reset()
    _tv_series.use("tv-series-translations")
    _tv_series.load_path_arg(series_id=series_id)
    return _tv_series.request()


def videos(series_id: int,
           language: str = None, include_video_language: str = None) -> dict:
    """Get the videos that belong to a TV show.
    
    include_video_language:
    filter the list results by language, supports more than one value by using a comma
    """
    _tv_series.reset()
    _tv_series.use("tv-series-videos")
    _tv_series.load_path_arg(series_id=series_id)
    _tv_series.language(language)
    if include_video_language is not None:
        _tv_series.load_query(include_video_language=include_video_language)
    return _tv_series.request()


def watch_providers(series_id: int) -> dict:
    """Get the list of streaming providers we have for a TV show.
    """
    _tv_series.reset()
    _tv_series.use("tv-series-watch-providers")
    _tv_series.load_path_arg(series_id=series_id)
    return _tv_series.request()


def add_rating(series_id: int, rating: int, guest_session_id: str = None) -> dict:
    """Rate a TV show and save it to your rated list.

    rating: 0~10
    """
    type_checking("rating", rating)
    _tv_series.reset()
    _tv_series.use("tv-series-add-rating")
    _tv_series.load_path_arg(series_id=series_id)
    _tv_series.choose_session_id(guest_session_id)
    _tv_series.load_json({"value": rating})
    return _tv_series.request()


def delete_rating(series_id: int, guest_session_id: str = None) -> dict:
    """Get the details of a TV show.
    """
    _tv_series.reset()
    _tv_series.use("tv-series-delete-rating")
    _tv_series.load_path_arg(series_id=series_id)
    _tv_series.choose_session_id(guest_session_id)
    return _tv_series.request()
