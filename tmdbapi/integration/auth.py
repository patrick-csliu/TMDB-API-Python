import webbrowser

import tmdbapi
from tmdbapi._core import query_yes_no


def create_session_id():
    """Create a session id"""
    request_token = tmdbapi.api3.authentication.create_request_token()["request_token"]
    approve_url = f"https://www.themoviedb.org/authenticate/{request_token}"
    webbrowser.open(approve_url, new=2)
    msg = f"Please approve the 3rd Party Authentication Request in your web browser. If the webpage doesn't open, you can copy and paste the following URL manually: {approve_url}.\nAfter approval, enter 'y' to continue."
    query_yes_no(msg)
    session_id = tmdbapi.api3.authentication.create_session(request_token)["session_id"]
    tmdbapi.setting["credential"].set(session_id=session_id)


def create_access_token():
    """Create a write permission access_token"""
    request_token = tmdbapi.api4.auth.create_request_token()["request_token"]
    approve_url = (
        f"https://www.themoviedb.org/auth/access?request_token={request_token}"
    )
    webbrowser.open(approve_url, new=2)
    msg = f"Please approve the 3rd Party Authentication Request in your web browser. If the webpage doesn't open, you can copy and paste the following URL manually: {approve_url}.\nAfter approval, enter 'y' to continue."
    query_yes_no(msg)
    response = tmdbapi.api4.auth.create_access_token(request_token)
    tmdbapi.setting["credential"].set(access_token=response["access_token"])
    tmdbapi.setting["credential"].set(account_object_id=response["account_object_id"])
    return response
