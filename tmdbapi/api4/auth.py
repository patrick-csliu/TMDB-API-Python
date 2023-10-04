"""API v4 auth category

"""

from tmdbapi._core import Tmdb

_AUTH_V4 = {
    "auth-create-access-token": {
        "method": "post",
        "params": [{"in": "body", "name": "RAW_BODY"}],
        "url": "/access_token",
    },
    "auth-create-request-token": {
        "method": "post",
        "params": [{"in": "body", "name": "RAW_BODY"}],
        "url": "/request_token",
    },
    "auth-logout": {
        "method": "delete",
        "params": [{"in": "body", "name": "RAW_BODY"}],
        "url": "/access_token",
    },
}


class _Auth(Tmdb):
    def __init__(self, info_var):
        super().__init__()
        self.category_path = "/auth"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(4)
        return self.request_raw(
            url=url,
        )


def create_access_token(request_token: str) -> dict:
    auth = _Auth(_AUTH_V4)
    auth.reset()
    auth.use("auth-create-access-token")
    auth.load_json({"request_token": request_token})
    return auth.request()


def create_request_token() -> dict:
    auth = _Auth(_AUTH_V4)
    auth.reset()
    auth.use("auth-create-request-token")
    auth.load_json({"redirect_to": "https://www.themoviedb.org/"})
    return auth.request()


def logout(access_token: str) -> dict:
    """Log out of a session."""
    auth = _Auth(_AUTH_V4)
    auth.reset()
    auth.use("auth-logout")
    auth.load_json({"access_token": access_token})
    return auth.request()
