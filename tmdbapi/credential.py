"""Manage TMDB credentials

Access Token Auth, API Key Auth, and session_id.
"""

import os
import pickle
from typing import TypedDict, Optional


# Store credentials in global variables
class CredentialType(TypedDict):
    access_token: Optional[str]
    api_key: Optional[str]
    session_id: Optional[str]
    account_id: Optional[int]
    account_object_id: Optional[str]

CREDENTIALS: CredentialType = {
    "access_token": None,
    "api_key": None,
    "session_id": None,
    "account_id": None,
    "account_object_id": None,
}

# Credential file path
CREDENTIAL_FILE = None


def set_credentials(access_token: str = None, api_key: str = None,
                     session_id: str = None, account_id: int = None,
                     account_object_id: str = None):
    """Set the key, IDs, and token.

    This function will store these thing in the module global variable.
    To keep the credentials in file, use `save_credentials()` after
    load it.

    Parameters
    ----------
    access_token : str, optional
        As Bearer token, if access_token is given, will use access_token 
        in api version3 (api3) by default, to change the api_key
        use `use_access_token(False)`. By default None
    api_key : str, optional
        For TMDB API version3, if access_token is given there is no
        needed of api_key. For more information see: 
        https://developer.themoviedb.org/docs/authentication-application.
        By default None
    session_id : str, optional
        An id give permission to access, by default None
    account_id : int, optional
        TMDB API version3 account id, by default None
    account_object_id : str, optional
        TMDB API version4 account id, by default None
    """
    global CREDENTIALS
    if access_token is not None:
        CREDENTIALS["access_token"] = access_token
    if api_key is not None:
        CREDENTIALS["api_key"] = api_key
    if session_id is not None:
        CREDENTIALS["session_id"] = session_id
    if account_id is not None:
        CREDENTIALS["account_id"] = account_id
    if account_object_id is not None:
        CREDENTIALS["account_object_id"] = account_object_id


def save_credentials(filepath: str = None):
    """Save the credential to file.

    This function saves the credentials to a file. Note that the 
    file is not encrypted, so it should be placed in a secure location.

    Parameters
    ----------
    filepath : str
        The file path where the credentials will be saved.
        If not specified, it will use the file loaded or saved 
        previously.
    """
    global CREDENTIAL_FILE
    path_given = filepath is not None
    path_exist = CREDENTIAL_FILE is not None
    if path_given:
        CREDENTIAL_FILE = filepath
    else:
        if path_exist:
            filepath = CREDENTIAL_FILE
        else:
            raise Exception("No filepath")
    with open(filepath, 'wb') as f:
        pickle.dump(CREDENTIALS, f)


def load_credentials(filepath: str):
    """Load the credentials from file.

    The format can't be customize, can only load from the file create
    by save_credentials().

    Parameters
    ----------
    filepath : str
        The file path where the credentials will be loaded.
    """
    global CREDENTIALS, CREDENTIAL_FILE
    with open(filepath, 'rb') as f:
        CREDENTIALS = pickle.load(f)
    CREDENTIAL_FILE = filepath


def set_env_var():
    """Put the credentials in the environment variables.
    """
    cred_env = {}
    var_names = {
        "access_token": "TMDB_ACCESS_TOKEN",
        "api_key": "TMDB_API_KEY",
        "session_id": "TMDB_SESSION_ID",
        "account_id": "TMDB_ACCOUNT_ID",
        "account_object_id": "TMDB_ACCOUNT_OBJECT_ID",
    }
    for k, v in CREDENTIALS.items():
        if v is not None:
            newname = var_names[k]
            cred_env[newname] = v
    if cred_env.get("TMDB_ACCOUNT_ID") is not None:
        cred_env["TMDB_ACCOUNT_ID"] = str(cred_env["TMDB_ACCOUNT_ID"])
    os.environ.update(cred_env)


def load_env_var(customize_var_names={}):
    """Read the credentials from the environment variables.

    Parameters
    ----------
    customize_var_names : dict, optional
        A dictionary that maps credential variable names to their 
        corresponding environment variable names if they are 
        different from the defaults.
        Default:
        ```
        {
            "access_token": "TMDB_ACCESS_TOKEN",
            "api_key": "TMDB_API_KEY",
            "session_id": "TMDB_SESSION_ID",
            "account_id": "TMDB_ACCOUNT_ID",
            "account_object_id": "TMDB_ACCOUNT_OBJECT_ID",
        }
        ```
        You can't change the keys in this dictionary.
    """
    global CREDENTIALS
    var_names = {
        "access_token": "TMDB_ACCESS_TOKEN",
        "api_key": "TMDB_API_KEY",
        "session_id": "TMDB_SESSION_ID",
        "account_id": "TMDB_ACCOUNT_ID",
        "account_object_id": "TMDB_ACCOUNT_OBJECT_ID",
    }
    var_names.update(customize_var_names)
    for k, v in var_names.items():
        CREDENTIALS[k] = os.environ.get(v)
    if CREDENTIALS.get("account_id") is not None:
        CREDENTIALS["account_id"] = str(CREDENTIALS["account_id"])
