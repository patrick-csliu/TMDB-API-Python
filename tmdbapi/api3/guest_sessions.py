"""API v3 guest sessions category

"""

from tmdbapi._core import Tmdb

_GUEST_SESSIONS_V3 = {
    "guest-session-rated-movies": {
        "method": "get",
        "params": [
            {"in": "path", "name": "guest_session_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "sort_by"},
        ],
        "url": "/{guest_session_id}/rated/movies",
    },
    "guest-session-rated-tv": {
        "method": "get",
        "params": [
            {"in": "path", "name": "guest_session_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "sort_by"},
        ],
        "url": "/{guest_session_id}/rated/tv",
    },
    "guest-session-rated-tv-episodes": {
        "method": "get",
        "params": [
            {"in": "path", "name": "guest_session_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "sort_by"},
        ],
        "url": "/{guest_session_id}/rated/tv/episodes",
    },
}


class _GuestSession(Tmdb):
    def __init__(self, info_var):
        super().__init__()
        self.category_path = "/guest_session"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url=url,
        )


def rated_movies(
    guest_session_id: str, language: str = None, page=1, asc_sort=True
) -> dict:
    """Get the rated movies for a guest session."""
    guest_session = _GuestSession(_GUEST_SESSIONS_V3)
    guest_session.reset()
    guest_session.use("guest-session-rated-movies")
    guest_session.load_path_arg(guest_session_id=guest_session_id)
    guest_session.language(language)
    guest_session.sortby(asc_sort)
    guest_session.load_query(page=page)
    return guest_session.request()


def rated_tv(
    guest_session_id: str, language: str = None, page=1, asc_sort=True
) -> dict:
    """Get the rated TV shows for a guest session."""
    guest_session = _GuestSession(_GUEST_SESSIONS_V3)
    guest_session.reset()
    guest_session.use("guest-session-rated-tv")
    guest_session.load_path_arg(guest_session_id=guest_session_id)
    guest_session.language(language)
    guest_session.sortby(asc_sort)
    guest_session.load_query(page=page)
    return guest_session.request()


def rated_tv_episodes(
    guest_session_id: str, language: str = None, page=1, asc_sort=True
) -> dict:
    """Get the rated TV episodes for a guest session."""
    guest_session = _GuestSession(_GUEST_SESSIONS_V3)
    guest_session.reset()
    guest_session.use("guest-session-rated-tv-episodes")
    guest_session.load_path_arg(guest_session_id=guest_session_id)
    guest_session.language(language)
    guest_session.sortby(asc_sort)
    guest_session.load_query(page=page)
    return guest_session.request()
