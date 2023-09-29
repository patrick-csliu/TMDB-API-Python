"""API v3 tv episodes category

"""

from tmdbapi._core import Tmdb


_TV_EPISODES_V3 = {
    "tv-episode-account-states": {
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "session_id"},
            {"in": "path", "name": "season_number"},
            {"in": "path", "name": "episode_number"},
            {"in": "query", "name": "guest_session_id"},
        ],
        "url": "/{series_id}/season/{season_number}/episode/{episode_number}/account_states",
    },
    "tv-episode-add-rating": {
        "method": "post",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "guest_session_id"},
            {"in": "query", "name": "session_id"},
            {"in": "body", "name": "RAW_BODY"},
            {"in": "header", "name": "Content-Type"},
            {"in": "path", "name": "season_number"},
            {"in": "path", "name": "episode_number"},
        ],
        "url": "/{series_id}/season/{season_number}/episode/{episode_number}/rating",
    },
    "tv-episode-changes-by-id": {
        "method": "get",
        "params": [{"in": "path", "name": "episode_id"}],
        "url": "/episode/{episode_id}/changes",
    },
    "tv-episode-credits": {
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "path", "name": "season_number"},
            {"in": "query", "name": "language"},
            {"in": "path", "name": "episode_number"},
        ],
        "url": "/{series_id}/season/{season_number}/episode/{episode_number}/credits",
    },
    "tv-episode-delete-rating": {
        "method": "delete",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "header", "name": "Content-Type"},
            {"in": "query", "name": "guest_session_id"},
            {"in": "query", "name": "session_id"},
            {"in": "path", "name": "season_number"},
            {"in": "path", "name": "episode_number"},
        ],
        "url": "/{series_id}/season/{season_number}/episode/{episode_number}/rating",
    },
    "tv-episode-details": {
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "path", "name": "season_number"},
            {"in": "path", "name": "episode_number"},
            {"in": "query", "name": "append_to_response"},
            {"in": "query", "name": "language"},
        ],
        "url": "/{series_id}/season/{season_number}/episode/{episode_number}",
    },
    "tv-episode-external-ids": {
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "path", "name": "season_number"},
            {"in": "path", "name": "episode_number"},
        ],
        "url": "/{series_id}/season/{season_number}/episode/{episode_number}/external_ids",
    },
    "tv-episode-images": {
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "include_image_language"},
            {"in": "query", "name": "language"},
            {"in": "path", "name": "season_number"},
            {"in": "path", "name": "episode_number"},
        ],
        "url": "/{series_id}/season/{season_number}/episode/{episode_number}/images",
    },
    "tv-episode-translations": {
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "path", "name": "season_number"},
            {"in": "path", "name": "episode_number"},
        ],
        "url": "/{series_id}/season/{season_number}/episode/{episode_number}/translations",
    },
    "tv-episode-videos": {
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "include_video_language"},
            {"in": "query", "name": "language"},
            {"in": "path", "name": "season_number"},
            {"in": "path", "name": "episode_number"},
        ],
        "url": "/{series_id}/season/{season_number}/episode/{episode_number}/videos",
    },
}


class _TvEpisodes(Tmdb):

    def __init__(self, info_var):
        super().__init__()
        self.base_path = "/tv"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url = url,
        )

_tv_episodes = _TvEpisodes(_TV_EPISODES_V3)


def details(series_id: int, season_number: int, episode_number: int,
            append_to_response="trailers,images,casts,translations",
            language: str = None) -> dict:
    """Query the details of a TV episode.
    """
    _tv_episodes.reset()
    _tv_episodes.use("tv-episode-details")
    _tv_episodes.load_path_arg(series_id=series_id,
                               season_number=season_number,
                               episode_number=episode_number)
    _tv_episodes.language(language)
    _tv_episodes.load_query(append_to_response=append_to_response)
    return _tv_episodes.request()


def account_states(series_id: int, season_number: int, episode_number: int,
                   guest_session_id: str = None) -> dict:
    """Get the rating, watchlist and " "favorite status.
    """
    _tv_episodes.reset()
    _tv_episodes.use("tv-episode-account-states")
    _tv_episodes.load_path_arg(series_id=series_id,
                               season_number=season_number,
                               episode_number=episode_number)
    _tv_episodes.choose_session_id(guest_session_id)
    return _tv_episodes.request()


def changes(episode_id: int) -> dict:
    """Get the recent changes for a TV episode.
    """
    _tv_episodes.reset()
    _tv_episodes.use("tv-episode-changes-by-id")
    _tv_episodes.load_path_arg(episode_id=episode_id)
    return _tv_episodes.request()


def credits(series_id: int, season_number: int, episode_number: int,
            language: str = None) -> dict:

    _tv_episodes.reset()
    _tv_episodes.use("tv-episode-credits")
    _tv_episodes.load_path_arg(series_id=series_id,
                               season_number=season_number,
                               episode_number=episode_number)
    _tv_episodes.language(language)
    return _tv_episodes.request()


def external_ids(series_id: int, season_number: int,
                 episode_number: int) -> dict:
    """Get a list of external IDs that have been added to a TV episode.
    """
    _tv_episodes.reset()
    _tv_episodes.use("tv-episode-external-ids")
    _tv_episodes.load_path_arg(series_id=series_id,
                               season_number=season_number,
                               episode_number=episode_number)
    return _tv_episodes.request()


def images(series_id: int, season_number: int, episode_number: int,
            language: str = None, include_image_language: str = None) -> dict:
    """Get the images that belong to a TV episode.
    """
    _tv_episodes.reset()
    _tv_episodes.use("tv-episode-images")
    _tv_episodes.load_path_arg(series_id=series_id,
                               season_number=season_number,
                               episode_number=episode_number)
    _tv_episodes.language(language)
    if include_image_language is not None:
        _tv_episodes.load_query(include_image_language=include_image_language)
    return _tv_episodes.request()


def translations(series_id: int, season_number: int,
                 episode_number: int) -> dict:
    """Get the translations that have been added to a TV episode.
    """
    _tv_episodes.reset()
    _tv_episodes.use("tv-episode-translations")
    _tv_episodes.load_path_arg(series_id=series_id,
                               season_number=season_number,
                               episode_number=episode_number)
    return _tv_episodes.request()


def videos(series_id: int, season_number: int, episode_number: int,
            language: str = None, include_video_language: str = None) -> dict:
    """Get the videos that belong to a TV episode.
    """
    _tv_episodes.reset()
    _tv_episodes.use("tv-episode-videos")
    _tv_episodes.load_path_arg(series_id=series_id,
                               season_number=season_number,
                               episode_number=episode_number)
    _tv_episodes.language(language)
    if include_video_language is not None:
        _tv_episodes.load_query(include_video_language=include_video_language)
    return _tv_episodes.request()


def add_rating(series_id: int, season_number: int, episode_number: int, rating,
               guest_session_id: str = None) -> dict:
    """Rate a TV episode and save it to your rated list.
    """
    _tv_episodes.reset()
    _tv_episodes.use("tv-episode-add-rating")
    _tv_episodes.load_path_arg(series_id=series_id,
                               season_number=season_number,
                               episode_number=episode_number)
    _tv_episodes.choose_session_id(guest_session_id)
    _tv_episodes.load_json({"value": rating})
    return _tv_episodes.request()


def delete_rating(series_id: int, season_number: int, episode_number: int,
                  guest_session_id: str = None) -> dict:
    """Delete your rating on a TV episode.
    """
    _tv_episodes.reset()
    _tv_episodes.use("tv-episode-delete-rating")
    _tv_episodes.load_path_arg(series_id=series_id,
                               season_number=season_number,
                               episode_number=episode_number)
    _tv_episodes.choose_session_id(guest_session_id)
    return _tv_episodes.request()
