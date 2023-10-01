"""API v3 account category

"""

from tmdbapi.credential import CREDENTIALS, set_credentials
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
        self.base_path = "/account"
        self.info_var = info_var

    def request(self) -> dict:
        """Send a request.
        """
        url = self.build_url(3)
        self.load_query(self.check_token())
        return self.request_raw(
            url = url,
        )
    
    def check_account_id(self):
        """Check if `account_id` exists.
        
        This method checks whether an `account_id` exists. If it doesn't, 
        it runs the 'details()' function to obtain the `account_id`.
        """
        if CREDENTIALS["account_id"] is None:
            details()

_account = _Account(_ACCOUNT_V3)


def details() -> dict:

    _account.reset()
    _account.use("account-details")
    json = _account.request()
    id = json['id']
    if CREDENTIALS["account_id"] != id:
        set_credentials(account_id=id)
    return json


def add_favorite(media_id: int, media_type: str, favorite=True) -> dict:

    type_checking("media_type", media_type)
    _account.reset()
    _account.use("account-add-favorite")
    _account.check_account_id()
    _account.load_path_arg(account_id=CREDENTIALS["account_id"])
    _account.load_json(
        {
            "media_type": media_type,
            "media_id": media_id,
            "favorite": favorite,
        }
    )
    return _account.request()


def add_to_watchlist(media_id: int, media_type: str, watchlist=True) -> dict:

    type_checking("media_type", media_type)
    _account.reset()
    _account.use("account-add-to-watchlist")
    _account.check_account_id()
    _account.load_path_arg(account_id=CREDENTIALS["account_id"])
    _account.load_json(
        {
            "media_type": media_type,
            "media_id": media_id,
            "watchlist": watchlist,
        }
    )
    return _account.request()


def favorite_movies(asc_sort=True, page=1,
                    language: str = None) -> dict:

    _account.reset()
    _account.use("account-get-favorites")
    _account.check_account_id()
    _account.load_path_arg(account_id=CREDENTIALS["account_id"])
    _account.sortby(asc_sort)
    _account.language(language)
    _account.load_query(page=page)
    return _account.request()


def favorite_tv_shows(asc_sort=True, page=1,
                      language: str = None) -> dict:

    _account.reset()
    _account.use("account-favorite-tv")
    _account.check_account_id()
    _account.load_path_arg(account_id=CREDENTIALS["account_id"])
    _account.sortby(asc_sort)
    _account.language(language)
    _account.load_query(page=page)
    return _account.request()


def get_list(page=1) -> dict:

    _account.reset()
    _account.use("account-lists")
    _account.check_account_id()
    _account.load_path_arg(account_id=CREDENTIALS["account_id"])
    _account.load_query(page=page)
    return _account.request()


def rated_movies(asc_sort=True, page=1,
                 language: str = None) -> dict:

    _account.reset()
    _account.use("account-rated-movies")
    _account.check_account_id()
    _account.load_path_arg(account_id=CREDENTIALS["account_id"])
    _account.sortby(asc_sort)
    _account.language(language)
    _account.load_query(page=page)
    return _account.request()


def rated_tv_shows(asc_sort=True, page=1,
                   language: str = None) -> dict:

    _account.reset()
    _account.use("account-rated-tv")
    _account.check_account_id()
    _account.load_path_arg(account_id=CREDENTIALS["account_id"])
    _account.sortby(asc_sort)
    _account.language(language)
    _account.load_query(page=page)
    return _account.request()


def rated_tv_episodes(asc_sort=True, page=1,
                      language: str = None) -> dict:

    _account.reset()
    _account.use("account-rated-tv-episodes")
    _account.check_account_id()
    _account.load_path_arg(account_id=CREDENTIALS["account_id"])
    _account.sortby(asc_sort)
    _account.language(language)
    _account.load_query(page=page)
    return _account.request()


def movie_watchlist(asc_sort=True, page=1,
                    language: str = None) -> dict:

    _account.reset()
    _account.use("account-watchlist-movies")
    _account.check_account_id()
    _account.load_path_arg(account_id=CREDENTIALS["account_id"])
    _account.sortby(asc_sort)
    _account.language(language)
    _account.load_query(page=page)
    return _account.request()


def tv_show_watchlist(asc_sort=True, page=1,
                      language: str = None) -> dict:

    _account.reset()
    _account.use("account-watchlist-tv")
    _account.check_account_id()
    _account.load_path_arg(account_id=CREDENTIALS["account_id"])
    _account.sortby(asc_sort)
    _account.language(language)
    _account.load_query(page=page)
    return _account.request()
