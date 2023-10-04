"""API v3 authentication category

"""

from tmdbapi._core import Tmdb

_AUTHENTICATION_V3 = {
    "authentication-create-guest-session": {
        "method": "get",
        "params": [],
        "url": "/guest_session/new",
    },
    "authentication-create-request-token": {
        "method": "get",
        "params": [],
        "url": "/token/new",
    },
    "authentication-create-session": {
        "method": "post",
        "params": [{"in": "body", "name": "RAW_BODY"}],
        "url": "/session/new",
    },
    "authentication-create-session-from-login": {
        "method": "post",
        "params": [{"in": "body", "name": "RAW_BODY"}],
        "url": "/token/validate_with_login",
    },
    "authentication-create-session-from-v4-token": {
        "method": "post",
        "params": [{"in": "body", "name": "RAW_BODY"}],
        "url": "/session/convert/4",
    },
    "authentication-delete-session": {
        "method": "delete",
        "params": [{"in": "body", "name": "RAW_BODY"}],
        "url": "/session",
    },
    "authentication-validate-key": {
        "method": "get",
        "params": [],
        "url": "",
    },
}


class _Authentication(Tmdb):
    def __init__(self, info_var):
        super().__init__()
        self.category_path = "/authentication"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url=url,
        )


def create_guest_session() -> dict:
    authentication = _Authentication(_AUTHENTICATION_V3)
    authentication.reset()
    authentication.use("authentication-create-guest-session")
    return authentication.request()


def create_request_token() -> dict:
    authentication = _Authentication(_AUTHENTICATION_V3)
    authentication.reset()
    authentication.use("authentication-create-request-token")
    return authentication.request()


def create_session(request_token: str) -> dict:
    authentication = _Authentication(_AUTHENTICATION_V3)
    authentication.reset()
    authentication.use("authentication-create-session")
    authentication.load_json({"request_token": request_token})
    return authentication.request()


def create_session_from_login(username: str, password: str, request_token: str) -> dict:
    authentication = _Authentication(_AUTHENTICATION_V3)
    authentication.reset()
    authentication.use("authentication-create-session-from-login")
    authentication.load_json(
        {
            "username": username,
            "password": password,
            "request_token": request_token,
        }
    )
    return authentication.request()


def create_session_from_v4_token(access_token: str) -> dict:
    authentication = _Authentication(_AUTHENTICATION_V3)
    authentication.reset()
    authentication.use("authentication-create-session-from-v4-token")
    authentication.load_json({"access_token": access_token})
    return authentication.request()


def delete_session(session_id: str) -> dict:
    authentication = _Authentication(_AUTHENTICATION_V3)
    authentication.reset()
    authentication.use("authentication-delete-session")
    authentication.load_json({"session_id": session_id})
    return authentication.request()


def validate_key() -> dict:
    authentication = _Authentication(_AUTHENTICATION_V3)
    authentication.reset()
    authentication.use("authentication-validate-key")
    return authentication.request()
