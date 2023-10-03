"""API v3 account category

"""

import tmdbapi
from tmdbapi._core import Tmdb
from tmdbapi.exceptions import type_checking

_ACCOUNT_V3 = {
    "account-add-favorite": {
        "method": "post",
        "params": [
            {"in": "path", "name": "account_id"},
            {"in": "query", "name": "session_id"},
            {"in": "body", "name": "RAW_BODY"},
        ],
        "url": "/{account_id}/favorite",
    },
    "account-add-to-watchlist": {
        "method": "post",
        "params": [
            {"in": "path", "name": "account_id"},
            {"in": "query", "name": "session_id"},
            {"in": "body", "name": "RAW_BODY"},
        ],
        "url": "/{account_id}/watchlist",
    },
    "account-details": {
        "method": "get",
        "params": [
            {"in": "path", "name": "account_id"},
            {"in": "query", "name": "session_id"},
        ],
        # "url": "/3/account/{account_id}",
        "url": "",
    },
    "account-favorite-tv": {
        "method": "get",
        "params": [
            {"in": "path", "name": "account_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "session_id"},
            {"in": "query", "name": "sort_by"},
        ],
        "url": "/{account_id}/favorite/tv",
    },
    "account-get-favorites": {
        "method": "get",
        "params": [
            {"in": "path", "name": "account_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "session_id"},
            {"in": "query", "name": "sort_by"},
        ],
        "url": "/{account_id}/favorite/movies",
    },
    "account-lists": {
        "method": "get",
        "params": [
            {"in": "path", "name": "account_id"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "session_id"},
        ],
        "url": "/{account_id}/lists",
    },
    "account-rated-movies": {
        "method": "get",
        "params": [
            {"in": "path", "name": "account_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "session_id"},
            {"in": "query", "name": "sort_by"},
        ],
        "url": "/{account_id}/rated/movies",
    },
    "account-rated-tv": {
        "method": "get",
        "params": [
            {"in": "path", "name": "account_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "session_id"},
            {"in": "query", "name": "sort_by"},
        ],
        "url": "/{account_id}/rated/tv",
    },
    "account-rated-tv-episodes": {
        "method": "get",
        "params": [
            {"in": "path", "name": "account_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "session_id"},
            {"in": "query", "name": "sort_by"},
        ],
        "url": "/{account_id}/rated/tv/episodes",
    },
    "account-watchlist-movies": {
        "method": "get",
        "params": [
            {"in": "path", "name": "account_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "session_id"},
            {"in": "query", "name": "sort_by"},
        ],
        "url": "/{account_id}/watchlist/movies",
    },
    "account-watchlist-tv": {
        "method": "get",
        "params": [
            {"in": "path", "name": "account_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "session_id"},
            {"in": "query", "name": "sort_by"},
        ],
        "url": "/{account_id}/watchlist/tv",
    },
}


class _Account(Tmdb):
    def __init__(self, info_var):
        super().__init__()
        self.category_path = "/account"
        self.info_var = info_var

    def request(self) -> dict:
        """Send a request."""
        self.check_account_id()
        self.load_path_arg(account_id=tmdbapi.setting["credential"]["account_id"])
        url = self.build_url(3)
        self.load_query(self.check_token())
        return self.request_raw(
            url=url,
        )

    def check_account_id(self):
        """Check if `account_id` exists.

        This method checks whether an `account_id` exists. If it doesn't,
        it runs the 'details()' function to obtain the `account_id`.
        """
        if not tmdbapi.setting["credential"].pass_check("account_id"):
            details()


def details() -> dict:
    account = _Account(_ACCOUNT_V3)
    account.reset()
    account.use("account-details")
    url = account.build_url(3)
    account.load_query(account.check_token())
    json = account.request_raw(url=url)
    id = json["id"]
    if tmdbapi.setting["credential"]["account_id"] != id:
        tmdbapi.setting["credential"].set(account_id=id)
    return json


def add_favorite(media_id: int, media_type: str, favorite=True) -> dict:
    account = _Account(_ACCOUNT_V3)
    type_checking("media_type", media_type)
    account.reset()
    account.use("account-add-favorite")
    account.load_json(
        {
            "media_type": media_type,
            "media_id": media_id,
            "favorite": favorite,
        }
    )
    return account.request()


def add_to_watchlist(media_id: int, media_type: str, watchlist=True) -> dict:
    account = _Account(_ACCOUNT_V3)
    type_checking("media_type", media_type)
    account.reset()
    account.use("account-add-to-watchlist")
    account.load_json(
        {
            "media_type": media_type,
            "media_id": media_id,
            "watchlist": watchlist,
        }
    )
    return account.request()


def favorite_movies(asc_sort=True, page=1, language: str = None) -> dict:
    account = _Account(_ACCOUNT_V3)
    account.reset()
    account.use("account-get-favorites")
    account.sortby(asc_sort)
    account.language(language)
    account.load_query(page=page)
    return account.request()


def favorite_tv_shows(asc_sort=True, page=1, language: str = None) -> dict:
    account = _Account(_ACCOUNT_V3)
    account.reset()
    account.use("account-favorite-tv")
    account.sortby(asc_sort)
    account.language(language)
    account.load_query(page=page)
    return account.request()


def get_list(page=1) -> dict:
    account = _Account(_ACCOUNT_V3)
    account.reset()
    account.use("account-lists")
    account.load_query(page=page)
    return account.request()


def rated_movies(asc_sort=True, page=1, language: str = None) -> dict:
    account = _Account(_ACCOUNT_V3)
    account.reset()
    account.use("account-rated-movies")
    account.sortby(asc_sort)
    account.language(language)
    account.load_query(page=page)
    return account.request()


def rated_tv_shows(asc_sort=True, page=1, language: str = None) -> dict:
    account = _Account(_ACCOUNT_V3)
    account.reset()
    account.use("account-rated-tv")
    account.sortby(asc_sort)
    account.language(language)
    account.load_query(page=page)
    return account.request()


def rated_tv_episodes(asc_sort=True, page=1, language: str = None) -> dict:
    account = _Account(_ACCOUNT_V3)
    account.reset()
    account.use("account-rated-tv-episodes")
    account.sortby(asc_sort)
    account.language(language)
    account.load_query(page=page)
    return account.request()


def movie_watchlist(asc_sort=True, page=1, language: str = None) -> dict:
    account = _Account(_ACCOUNT_V3)
    account.reset()
    account.use("account-watchlist-movies")
    account.sortby(asc_sort)
    account.language(language)
    account.load_query(page=page)
    return account.request()


def tv_show_watchlist(asc_sort=True, page=1, language: str = None) -> dict:
    account = _Account(_ACCOUNT_V3)
    account.reset()
    account.use("account-watchlist-tv")
    account.sortby(asc_sort)
    account.language(language)
    account.load_query(page=page)
    return account.request()
