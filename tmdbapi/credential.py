"""Manage TMDB Credentials

Provides functions for setting, saving, loading, and managing TMDB API
credentials, including access tokens, API keys, session IDs, account 
IDs, and account object IDs.
"""

import os
import pickle
from pathlib import Path
from typing import Optional, TypedDict

import tmdbapi
import tmdbapi._core


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
    """Set API credentials.

    This function stores the provided credentials in module global 
    variables. To persist the credentials in a file, use 
    `save_credentials()` after loading them.

    Parameters
    ----------
    access_token : str, optional
        The Bearer token. If provided, it will be used as the access 
        token in API version 3 (api3) by default. To change the API key
        , use `settings(use_access_token=False)`. Default is None.
    api_key : str, optional
        The API key for TMDB API version 3. If an access_token is provided, 
        there is no need for an api_key. For more information, 
        see: https://developer.themoviedb.org/docs/authentication-application.
        Default is None.
    session_id : str, optional
        An ID granting permission to access resources. Default is None.
    account_id : int, optional
        The TMDB API version 3 account ID. Default is None.
    account_object_id : str, optional
        The TMDB API version 4 account ID. Default is None.
    """
    global CREDENTIALS
    pre_cred = CREDENTIALS.copy()
    if access_token is not None:
        CREDENTIALS["access_token"] = access_token
        tmdbapi._core.SETTINGS["use_access_token"] = True
    if api_key is not None:
        CREDENTIALS["api_key"] = api_key
    if session_id is not None:
        CREDENTIALS["session_id"] = session_id
    if account_id is not None:
        CREDENTIALS["account_id"] = account_id
    if account_object_id is not None:
        CREDENTIALS["account_object_id"] = account_object_id
    if CREDENTIAL_FILE is not None:
        save_credentials()
    change = dict(set(pre_cred.items()) ^ set(CREDENTIALS.items()))
    if change:
        change_str = ", ".join(change)
        tmdbapi.LOGGER.info(f"Credential update: {change_str}")


def save_credentials(filepath: str = None):
    """Save the credentials to file.

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
            raise ValueError("No filepath")
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'wb') as f:
        pickle.dump(CREDENTIALS, f)
    tmdbapi.LOGGER.info(f"Credential store at {path.absolute()}")


def load_credentials(filepath: str):
    """Load the credentials from file.

    The format cannot be customized and can only be loaded from a file
    created by `save_credentials()`.

    Parameters
    ----------
    filepath : str
        The file path where the credentials will be loaded from.
    """
    global CREDENTIALS, CREDENTIAL_FILE
    with open(filepath, 'rb') as f:
        CREDENTIALS = pickle.load(f)
    CREDENTIAL_FILE = filepath
    if CREDENTIALS["access_token"] is None:
        tmdbapi._core.SETTINGS["use_access_token"] = False
    else:
        tmdbapi._core.SETTINGS["use_access_token"] = True
    tmdbapi.LOGGER.info(f"Credential loaded successful.")


def set_env_var():
    """Set credentials as environment variables.
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
    tmdbapi.LOGGER.info(f"Set credentials as environment variables.")


def load_env_var(customize_var_names={}):
    """Load credentials from environment variables.

    Note: This function will clear previous credential, to save run
    `save_credentials`

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
        CREDENTIALS["account_id"] = int(CREDENTIALS["account_id"])
    if CREDENTIALS["access_token"] is not None:
        tmdbapi._core.SETTINGS["use_access_token"] = True
    tmdbapi.LOGGER.info(f"Load credentials from environment variables.")
