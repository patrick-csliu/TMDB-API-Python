"""API v3 tv seasons category

"""

from tmdbapi._core import Tmdb
from tmdbapi.exceptions import type_checking

_TV_SEASONS_V3 = {
    "tv-season-account-states": {
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "session_id"},
            {"in": "query", "name": "guest_session_id"},
            {"in": "path", "name": "season_number"},
        ],
        "url": "/{series_id}/season/{season_number}/account_states",
    },
    "tv-season-aggregate-credits": {
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "language"},
            {"in": "path", "name": "season_number"},
        ],
        "url": "/{series_id}/season/{season_number}/aggregate_credits",
    },
    "tv-season-changes-by-id": {
        "method": "get",
        "params": [
            {"in": "query", "name": "end_date"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "start_date"},
            {"in": "path", "name": "season_id"},
        ],
        "url": "/season/{season_id}/changes",
    },
    "tv-season-credits": {
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "path", "name": "season_number"},
            {"in": "query", "name": "language"},
        ],
        "url": "/{series_id}/season/{season_number}/credits",
    },
    "tv-season-details": {
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "path", "name": "season_number"},
            {"in": "query", "name": "append_to_response"},
            {"in": "query", "name": "language"},
        ],
        "url": "/{series_id}/season/{season_number}",
    },
    "tv-season-external-ids": {
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "path", "name": "season_number"},
        ],
        "url": "/{series_id}/season/{season_number}/external_ids",
    },
    "tv-season-images": {
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "include_image_language"},
            {"in": "query", "name": "language"},
            {"in": "path", "name": "season_number"},
        ],
        "url": "/{series_id}/season/{season_number}/images",
    },
    "tv-season-translations": {
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "path", "name": "season_number"},
        ],
        "url": "/{series_id}/season/{season_number}/translations",
    },
    "tv-season-videos": {
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "include_video_language"},
            {"in": "query", "name": "language"},
            {"in": "path", "name": "season_number"},
        ],
        "url": "/{series_id}/season/{season_number}/videos",
    },
    "tv-season-watch-providers": {
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "language"},
            {"in": "path", "name": "season_number"},
        ],
        "url": "/{series_id}/season/{season_number}/watch/providers",
    },
}


class _TvSeasons(Tmdb):
    def __init__(self, info_var):
        super().__init__()
        self.category_path = "/tv"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url=url,
        )


def details(
    series_id: int,
    season_number: int,
    append_to_response="trailers,images,casts,translations",
    language: str = None,
) -> dict:
    """Query the details of a TV season."""
    tv_seasons = _TvSeasons(_TV_SEASONS_V3)
    tv_seasons.reset()
    tv_seasons.use("tv-season-details")
    tv_seasons.load_path_arg(series_id=series_id, season_number=season_number)
    tv_seasons.language(language)
    tv_seasons.load_query(append_to_response=append_to_response)
    return tv_seasons.request()


def account_states(
    series_id: int, season_number: int, guest_session_id: str = None
) -> dict:
    """Get the rating, watchlist and " "favorite status."""
    tv_seasons = _TvSeasons(_TV_SEASONS_V3)
    tv_seasons.reset()
    tv_seasons.use("tv-season-account-states")
    tv_seasons.load_path_arg(series_id=series_id, season_number=season_number)
    tv_seasons.choose_session_id(guest_session_id)
    return tv_seasons.request()


def aggregate_credits(series_id: int, season_number: int, language: str = None) -> dict:
    """Get the aggregate credits (cast and crew) that have been
    added to a TV season.
    """
    tv_seasons = _TvSeasons(_TV_SEASONS_V3)
    tv_seasons.reset()
    tv_seasons.use("tv-season-aggregate-credits")
    tv_seasons.load_path_arg(series_id=series_id, season_number=season_number)
    tv_seasons.language(language)
    return tv_seasons.request()


def changes(season_id: int, start_date="", end_date="", page=1) -> dict:
    """Get the recent changes for a TV season.

    `start_date` and `start_date` is lte and gte
    Format: YYYY-MM-DD
    """
    tv_seasons = _TvSeasons(_TV_SEASONS_V3)
    tv_seasons.reset()
    tv_seasons.use("tv-season-changes-by-id")
    tv_seasons.load_path_arg(season_id=season_id)
    if start_date != "":
        type_checking("date", start_date)
        tv_seasons.load_query(start_date=start_date)
    if end_date != "":
        type_checking("date", end_date)
        tv_seasons.load_query(end_date=end_date)
    tv_seasons.load_query(page=page)
    return tv_seasons.request()


def credits(series_id: int, season_number: int, language: str = None) -> dict:
    tv_seasons = _TvSeasons(_TV_SEASONS_V3)
    tv_seasons.reset()
    tv_seasons.use("tv-season-credits")
    tv_seasons.load_path_arg(series_id=series_id, season_number=season_number)
    tv_seasons.language(language)
    return tv_seasons.request()


def external_ids(series_id: int, season_number: int) -> dict:
    """Get a list of external IDs that have been added to a TV season."""
    tv_seasons = _TvSeasons(_TV_SEASONS_V3)
    tv_seasons.reset()
    tv_seasons.use("tv-season-external-ids")
    tv_seasons.load_path_arg(series_id=series_id, season_number=season_number)
    return tv_seasons.request()


def images(
    series_id: int,
    season_number: int,
    language: str = None,
    include_image_language: str = None,
) -> dict:
    """Get the images that belong to a TV season.

    include_image_language:
    specify a comma separated list of ISO-639-1 values to query,
    for example: en,null
    """
    tv_seasons = _TvSeasons(_TV_SEASONS_V3)
    tv_seasons.reset()
    tv_seasons.use("tv-season-images")
    tv_seasons.load_path_arg(series_id=series_id, season_number=season_number)
    tv_seasons.language(language)
    if include_image_language is not None:
        tv_seasons.load_query(include_image_language=include_image_language)
    return tv_seasons.request()


def translations(series_id: int, season_number: int) -> dict:
    """Get the translations for a TV season."""
    tv_seasons = _TvSeasons(_TV_SEASONS_V3)
    tv_seasons.reset()
    tv_seasons.use("tv-season-translations")
    tv_seasons.load_path_arg(series_id=series_id, season_number=season_number)
    return tv_seasons.request()


def videos(
    series_id: int,
    season_number: int,
    language: str = None,
    include_video_language: str = None,
) -> dict:
    """Get the videos that belong to a TV season.

    include_video_language:
    filter the list results by language, supports more than one value by using a comma
    """
    tv_seasons = _TvSeasons(_TV_SEASONS_V3)
    tv_seasons.reset()
    tv_seasons.use("tv-season-videos")
    tv_seasons.load_path_arg(series_id=series_id, season_number=season_number)
    tv_seasons.language(language)
    if include_video_language is not None:
        tv_seasons.load_query(include_video_language=include_video_language)
    return tv_seasons.request()


def watch_providers(series_id: int, season_number: int, language: str = None) -> dict:
    """Get the list of streaming providers we have for a TV season."""
    tv_seasons = _TvSeasons(_TV_SEASONS_V3)
    tv_seasons.reset()
    tv_seasons.use("tv-season-watch-providers")
    tv_seasons.load_path_arg(series_id=series_id, season_number=season_number)
    tv_seasons.language(language)
    return tv_seasons.request()
