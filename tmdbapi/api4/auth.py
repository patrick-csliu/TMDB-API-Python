"""API v4 auth category

"""

import webbrowser
from tmdbapi._core import Tmdb, query_yes_no

from tmdbapi import credential


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
        self.base_path = "/auth"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(4)
        return self.request_raw(
            url = url,
        )

_auth = _Auth(_AUTH_V4)


def create_access_token(request_token: str) -> dict:

    _auth.reset()
    _auth.use("auth-create-access-token")
    _auth.load_json({"request_token": request_token})
    return _auth.request()


def  create_request_token() -> dict:

    _auth.reset()
    _auth.use("auth-create-request-token")
    _auth.load_json({"redirect_to": "https://www.themoviedb.org/"})
    return _auth.request()


def logout(access_token: str) -> dict:
    """Log out of a session.
    """
    _auth.reset()
    _auth.use("auth-logout")
    _auth.load_json({"access_token": access_token})
    return _auth.request()


def access_token():
    """Create a write permission access_token
    """
    request_token = create_request_token()["request_token"]
    approve_url = f'https://www.themoviedb.org/auth/access?request_token={request_token}'
    webbrowser.open(approve_url, new=2)
    msg = f"Please approve the 3rd Party Authentication Request in your web browser. If the webpage doesn't open, you can copy and paste the following URL manually: {approve_url}.\nAfter approval, enter 'y' to continue."
    query_yes_no(msg)
    response =  create_access_token(request_token)
    credential.set_credentials(access_token=response["access_token"])
    return response
