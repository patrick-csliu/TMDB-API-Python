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
    tmdbapi.creds.set_credentials(session_id=session_id)


def access_token():
    """Create a write permission access_token"""
    request_token = create_request_token()["request_token"]
    approve_url = (
        f"https://www.themoviedb.org/auth/access?request_token={request_token}"
    )
    webbrowser.open(approve_url, new=2)
    msg = f"Please approve the 3rd Party Authentication Request in your web browser. If the webpage doesn't open, you can copy and paste the following URL manually: {approve_url}.\nAfter approval, enter 'y' to continue."
    query_yes_no(msg)
    response = create_access_token(request_token)
    creds.set_credentials(access_token=response["access_token"])
    return response
