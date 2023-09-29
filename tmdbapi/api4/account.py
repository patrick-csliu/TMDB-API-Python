"""API v4 account category

"""


from tmdbapi._core import Tmdb, use_access_token
from tmdbapi.credential import CREDENTIALS


_ACCOUNT_V4 = {
    "account-favorite-movies": {
        "method": "get",
        "params": [
            {"in": "path", "name": "account_object_id"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "language"},
        ],
        "url": "/movie/favorites",
    },
    "account-favorite-tv": {
        "method": "get",
        "params": [
            {"in": "path", "name": "account_object_id"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "language"},
        ],
        "url": "/tv/favorites",
    },
    "account-lists": {
        "method": "get",
        "params": [
            {"in": "path", "name": "account_object_id"},
            {"in": "query", "name": "page"},
        ],
        "url": "/lists",
    },
    "account-movie-recommendations": {
        "method": "get",
        "params": [
            {"in": "path", "name": "account_object_id"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "language"},
        ],
        "url": "/movie/recommendations",
    },
    "account-movie-watchlist": {
        "method": "get",
        "params": [
            {"in": "path", "name": "account_object_id"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "language"},
        ],
        "url": "/movie/watchlist",
    },
    "account-rated-movies": {
        "method": "get",
        "params": [
            {"in": "path", "name": "account_object_id"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "language"},
        ],
        "url": "/movie/rated",
    },
    "account-rated-tv": {
        "method": "get",
        "params": [
            {"in": "path", "name": "account_object_id"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "language"},
        ],
        "url": "/tv/rated",
    },
    "account-tv-recommendations": {
        "method": "get",
        "params": [
            {"in": "path", "name": "account_object_id"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "language"},
        ],
        "url": "/tv/recommendations",
    },
    "account-tv-watchlist": {
        "method": "get",
        "params": [
            {"in": "path", "name": "account_object_id"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "language"},
        ],
        "url": "/tv/watchlist",
    },
}


class _Account(Tmdb):

    def __init__(self, info_var):
        super().__init__()
        self.base_path = "/4/account/{account_object_id}"
        self.info_var = info_var

    def request(self) -> dict:
        use_access_token(True)
        url = self.build_url(4)
        return self.request_raw(
            url = url,
        )
    
    def check_account_object_id(self):
        """Check whether `account_object_id` exists
        """
        if CREDENTIALS["account_object_id"] is None:
            raise Exception("Need account_object_id")
        
    def get(self, use_name, page, language) -> dict:
        """Wrap for same process
        """
        self.reset()
        self.use(use_name)
        self.check_account_object_id()
        self.load_path_arg(account_object_id=CREDENTIALS["account_object_id"])
        self.language(language)
        self.load_query(page=page)
        return self.request()

_account = _Account(_ACCOUNT_V4)


def lists(page=1) -> dict:
    """Get all of the lists you've created.
    """
    _account.reset()
    _account.use("account-lists")
    _account.check_account_object_id()
    _account.load_path_arg(account_object_id=CREDENTIALS["account_object_id"])
    _account.load_query(page=page)
    return _account.request()


def favorite_movies(page=1, language: str = None) -> dict:
    """Get a user's list of favorite movies.
    """
    return _account.get("account-favorite-movies",
                        page=page, language=language)


def favorite_tv_shows(page=1, language: str = None) -> dict:
    """Get a user's list of favorite TV shows.
    """
    return _account.get("account-favorite-tv",
                        page=page, language=language)


def rated_movies(page=1, language: str = None) -> dict:
    """Get a user's rated movies.
    """
    return _account.get("account-rated-movies",
                        page=page, language=language)


def rated_tv_shows(page=1, language: str = None) -> dict:
    """Get a user's rated TV shows.
    """
    return _account.get("account-rated-tv",
                        page=page, language=language)


def recommended_movies(page=1, language: str = None) -> dict:
    """Get a user's list of recommended movies.
    """
    return _account.get("account-movie-recommendations",
                        page=page, language=language)


def recommended_tv_shows(page=1, language: str = None) -> dict:
    """Get a user's list of recommended TV shows.
    """
    return _account.get("account-tv-recommendations",
                        page=page, language=language)


def watchlist_movies(page=1, language: str = None) -> dict:
    """Get a user's movie watchlist.
    """
    return _account.get("account-movie-watchlist",
                        page=page, language=language)


def watchlist_tv_shows(page=1, language: str = None) -> dict:
    """Get a user's TV watchlist.
    """
    return _account.get("account-tv-watchlist",
                        page=page, language=language)
