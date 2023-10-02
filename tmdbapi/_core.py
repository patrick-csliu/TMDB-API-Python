"""
The Core of the TMDb Request API
"""

import sys
import webbrowser
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
from typing import Optional, TypedDict

import requests

import tmdbapi

from .exceptions import TmdbApiException, STATUS

# try:
#     from functools import lru_cache
# except ImportError:
#     from backports.functools_lru_cache import lru_cache


API_BASE = "https://api.themoviedb.org"

# SETTINGS
class SettingsType(TypedDict):
    use_access_token: bool
    timeout: float | tuple[float, float] | tuple[float, None] | None
    default_language: Optional[str]
    default_region: Optional[str]
    use_session: bool
    log_file: Optional[str]

SETTINGS: SettingsType = {
        # "tmdb_cache_enable": True,
        "use_access_token": False,
        "timeout": None,
        "default_language": None,
        "default_region": None,
        "use_session": False,
        "log_file": None,
}


class Tmdb:
    """The Tmdb class provides a Python interface for making requests to the TMDb (The Movie Database) API.

    Attributes:
        _headers (dict): Default headers for API requests.

        session (requests.Session): A session for making HTTP requests.

        base_path (str): The base path for each API category.

        info_var (dict): The information dictionary for each API category. This dictionary contains HTTP request 
            method, path, and parameters for each service.

    Methods:
        __init__(self): Initialize a new instance of the Tmdb class.

        _authentication(self, headers: dict, params: dict) -> tuple[dict, dict]: Set the headers and query parameters
            based on the 'use_access_token' setting.

        check_token(self) -> dict: Check if the application is using an access_token or api_key and return the
            appropriate query parameters.

        choose_session_id(self, guest_session_id: str): Choose a session_id based on the provided `guest_session_id`
            or use the default `session_id`.

        use(self, name: str): Select a service from the information dictionary.

        load_query(self, query={}, **kwargs): Update the query parameters for the API request.

        load_path_arg(self, args={}, **kwargs): Update the path parameters in the relative URL.

        load_json(self, json_dict: dict): Provide a JSON payload for the API request.

        build_url(self, version: int) -> str: Build the URL for the API request.

        sortby(self, asc: bool): Update the query parameters with valid values for sorting.

        language(self, lang: str = None): Update the language parameter in the query.

        region(self, region: str = None): Update the region parameter in the query.
        
        reset(self): Clear all content in class variables.

        check_params(self, params: dict) -> bool: Check if the given parameters keys are all valid.

        request_raw(self, url: str, method: str = None, params: dict = None, data=None, json: dict = None) -> dict: Send
            the API request and handle the response.

    """
    _headers = {"accept": "application/json",}
    session = requests.Session()
    base_path = ""
    info_var = None

    def __init__(self):
        self._ref: str = None    # (Relative) path for service
        self._method: str = None # Http(s) request method
        self._json: dict = None   # Json payload
        self._query = {}    # Queries for url
        self._path_args = {}    # the parameter to replace the anchor
                                # in _ref

    # @property
    # def wait_on_rate_limit(self):
    #     return SETTINGS["tmdb_wait_on_rate_limit"]

    # @wait_on_rate_limit.setter
    # def wait_on_rate_limit(self, wait_on_rate_limit):
    #     SETTINGS["tmdb_wait_on_rate_limit"] = wait_on_rate_limit

    # @property
    # def cache(self):
    #     return SETTINGS["tmdb_cache_enable"]

    # @cache.setter
    # def cache(self, cache):
    #     SETTINGS["tmdb_cache_enable"] = cache

    # @staticmethod
    # @lru_cache()
    # def cached_request(method, url, params, headers):
    #     return requests.request(method, url, params=params,
    #                             proxies=SETTINGS["tmdb_proxies"], headers=headers,
    #                             timeout=SETTINGS["timeout"])

    # def cache_clear(self):
    #     return self.cached_request.cache_clear()
    def _create_session_id(self):
        """Create a session id
        """
        request_token = tmdbapi.api3.authentication.create_request_token()["request_token"]
        approve_url = f'https://www.themoviedb.org/authenticate/{request_token}'
        webbrowser.open(approve_url, new=2)
        msg = f"Please approve the 3rd Party Authentication Request in your web browser. If the webpage doesn't open, you can copy and paste the following URL manually: {approve_url}.\nAfter approval, enter 'y' to continue."
        query_yes_no(msg)
        session_id =  tmdbapi.api3.authentication.create_session(request_token)["session_id"]
        tmdbapi.credential.set_credentials(session_id=session_id)

    def _authentication(self, headers: dict, params: dict) -> tuple[dict, dict]:
        """Set the headers and query parameters based on the 'use_access_token' setting.

        Parameters
        ----------
        headers : dict
            The headers dictionary.
        params : dict
            The headers dictionary. 

        Returns
        -------
        tuple[dict, dict]
            (headers, query)
            A tuple containing the updated headers and query parameters.
        """
        if SETTINGS["use_access_token"]:
            token = tmdbapi.credential.CREDENTIALS["access_token"]
            headers["Authorization"] = f"Bearer {token}"
        else:
            if tmdbapi.credential.CREDENTIALS["api_key"] is None:
                tmdbapi.LOGGER.error("No api_key given, please set the api_key")
                raise Exception("No api_key given, please set the api_key")
            else:
                params["api_key"] = tmdbapi.credential.CREDENTIALS["api_key"]
        return headers, params

    def check_token(self, state=0) -> Optional[dict]:
        """Check if the application is currently using an access_token or api_key.

        If an access_token is used, there is no need for session_id.

        Returns
        -------
        dict
            A dictionary with query parameters.
        """
        # Check if session_id exists. If it doesn't, force the use of 
        # access_token. If both session_id and access_token don't exist
        # , then create session_id.
        has_session_id =  tmdbapi.credential.CREDENTIALS["session_id"] is not None
        if SETTINGS["use_access_token"]:
            return {}
        else:
            if has_session_id:
                return {"session_id": tmdbapi.credential.CREDENTIALS["session_id"]}
            else:
                if state == 0:
                    settings(use_access_token=True)
                    return self.check_token(1)
                elif state == 1:
                    tmdbapi.LOGGER.info("No session_id, creating a session_id.")
                    self._create_session_id()
                    return self.check_token(2)
                else:
                    tmdbapi.LOGGER.error("Unable to retrieve the session_id.")
                    RuntimeError("Unable to retrieve the session_id.")

    def choose_session_id(self, guest_session_id: str):
        """Choose a session_id based on the provided 'guest_session_id' or use the default 'session_id'.

        Parameters
        ----------
        guest_session_id : str
            The guest session ID.
        """
        if guest_session_id is None:
            self._query.update(self.check_token())
        else:
            self._query.update(guest_session_id=guest_session_id)

    def use(self, name: str):
        """Select a service from the information dictionary.

        Parameters
        ----------
        name : str
            The key in the information dictionary.
        """
        self._ref = self.info_var[name]["url"]
        self._method = self.info_var[name]["method"]
        self._name = name

    def load_query(self, query={}, **kwargs):
        """Update the query parameters.

        Parameters
        ----------
        query : dict, optional
            The query parameters dictionary.
        """
        self._query.update(query)
        self._query.update(kwargs)

    def load_path_arg(self, args={}, **kwargs):
        """Update the parameters in the relative URL (_rel).

        Example: The account.details have the relative URL = "/{account_id}/favorite"
        And therefor it has one parameter `account_id`.
        This parameter can be assigned using `load_path_arg(account_id=xxx)`.

        Parameters
        ----------
        args : dict, optional
        """
        self._path_args.update(args)
        self._path_args.update(kwargs)

    def load_json(self, json_dict: dict):
        """Provide a JSON payload for the request.

        Parameters
        ----------
        json_dict : dict
            The JSON payload dictionary.
        """
        self._json = json_dict

    def build_url(self, version: int) -> str:
        """Build the url for request.

        Parameters
        ----------
        version : int
            The API version (3 or 4).

        Returns
        -------
        str
            The URL without query parameters.
        """
        ref = f"{self.base_path}{self._ref}"
        ref = ref.format(**self._path_args)
        return f"{API_BASE}/{version}{ref}"

    def sortby(self, asc: bool):
        """Update the query by specifying ascending or descending sorting order.

        Parameters
        ----------
        asc : bool
            True: Sort in ascending order.
            False: Sort in descending order.
        """
        if asc:
            s =  {"sort_by": "created_at.asc"}
        else:
            s =  {"sort_by": "created_at.desc"}
        self._query.update(s)
    
    def language(self, lang: str = None):
        """Update the language parameter in the query.

        If 'lang' is provided, it will be used; otherwise, the default language setting will be used.

        Parameters
        ----------
        lang : str, optional
            Format: `language-COUNTRY`.
            Example: 'zh-TW', 'en-US'.
            See: https://developer.themoviedb.org/docs/languages
        """
        if lang is not None:
            s = {"language": lang}
        elif SETTINGS["default_language"] is not None:
            s = {"language": SETTINGS["default_language"]}
        else:
            s = {}
        self._query.update(s)

    def region(self, region: str = None):
        """Update the region parameter in the query.

        Parameters
        ----------
        region : str, optional
            Format: ISO 3166-1
        """
        if region is not None:
            s = {"region": region}
        elif SETTINGS["default_language"] is not None:
            s = {"region": SETTINGS["default_region"]}
        else:
            s = {}
        self._query.update(s)

    def reset(self):
        """Reset all content in instance variables.
        """
        self._ref = None
        self._method = None
        self._json = None
        self._query = {}
        self._path_args = {}

    def check_params(self, params: dict) -> bool:
        """Check the givin parameters keys are all in the valid.

        Compare to the information dictionary, check all in it.

        Parameters
        ----------
        params : dict
            The dictionary containing function input parameters.

        Returns
        -------
        bool
            Return True if pass the check; otherwise, return False.
        """
        params_name = []
        for p in self.info_var[self._name]["params"]:
            params_name.append(p["name"])
        return set(params.keys()).issubset(set(params_name))

    def request_raw(self, url: str, method: str = None, params: dict = None, data=None, json: dict = None) -> dict:
        """Send a request and handle the response.

        Parameters
        ----------
        url : str
            The URL without query parameters.
        method : str, optional
            The request method, default is None.
        params : dict, optional
            The query parameters, default is None.
        data : _type_, optional
            The payload data, default is None.
        json : dict, optional
            The JSON payload, default is None.

        Returns
        -------
        dict
             A JSON-formatted response.

        Raises
        ------
        TmdbApiException
            If the action is not successful.
        """
        # set method, query(params), headers, json payload
        #
        if method is None:
            method = self._method.upper()
        else:
            method = method.upper()
        if params is None:
            params = self._query
        if json is None:
            json = self._json
        headers, params = self._authentication(headers=self._headers.copy(),
                                               params=params)
        if json is not None:
            headers["content-type"] = "application/json"
        
        # debug print #
        print("json:", json)
        print(method, headers)

        # send request to tmdb api
        #
        if SETTINGS["use_session"]:
            request = self.session
        else:
            request = requests
        # if self.cache and method == "GET":
            # response = self.cached_request(method, url, params=params,
            #                                headers=headers)
            # response = request.request(method, url, params=params,
            #                            headers=headers)
        # else:
        response = request.request(method, url, data=data,
                                    json=json, #proxies=self.proxies,
                                    params=params, headers=headers,
                                    timeout=SETTINGS["timeout"])

        headers = response.headers
        header_status_code = response.status_code
        # debug print #
        tmdbapi.LOGGER.info(f"status_code: {header_status_code}, {method}: {response.url}")
        # handle response
        has_content = headers.get("content-length", "1") != "0"
        if has_content:
            if headers.get("Content-Type", "").startswith("application/json"):
                content =  response.json()
            else:
                content = response.text
                TmdbApiException("The content is not json. Content:",
                                 content)
        else:
            TmdbApiException("No content.")
        if isinstance(content, dict):
            is_success = content.get("success", None)
            if is_success is not None and is_success == False:
                raise TmdbApiException(content["status_message"])
        return content


def credential_check(needed: str) -> bool:
    """Check if the needed credentials exist.

    Parameters
    ----------
    needed : str
        valid values:
        'access_token', 'api_key', 'session_id', 'account_object_id'

    Returns
    -------
    bool
        Return True if the needed credential exist.

    Raises
    ------
    ExceptionGroup
        If the needed credentials do not exist.
    """
    token_type = (
        "access_token",
        "api_key",
        "session_id",
        "account_object_id"
    )
    token_exist = [tmdbapi.credential.CREDENTIALS[token] is not None for token in token_type]
    exceptions = [
        Exception("You must set up an access token before making this request. Please configure your access token settings to proceed."),
        Exception("You must set up an api_key before making this request. Please configure your api_key settings to proceed."),
        Exception("You must set up an session_id before making this request. Please configure your session_id settings to proceed."),
        Exception("You must set up an account_object_id before making this request. Please configure your account_object_id settings to proceed."),
    ]
    errors = []
    for i in range(4):
        if token_type[i] in needed and not token_exist[i]:
            errors.append(exceptions[i])
    if len(errors) != 0:
        raise ExceptionGroup("Missing credential", errors)
    else:
        return True


def settings(**kwargs):
    """Modify settings

    ```
    Default settings:
    {
        "use_access_token": False,
        "timeout": None,
        "default_language": None,
        "default_region": None,
        "use_session": False,
        "log_file": None,
    }
    ```
    Raises
    ------
    ValueError
        If the setting not in the Settings options.
    """
    if not set(kwargs.keys()).issubset(SETTINGS.keys()):
        raise KeyError("The setting you have provided is not among the available options.")
    pre_setting = SETTINGS.copy()
    if "use_session" in kwargs.keys() and kwargs["use_session"] != SETTINGS["use_session"]:
        if kwargs["use_session"]:
            Tmdb.session = requests.Session()
        else:
            Tmdb.session = None
    if "log_file" in kwargs.keys() and kwargs["log_file"] != SETTINGS["log_file"]:
        if kwargs["log_file"] is not None:
            path = kwargs["log_file"]
            Path(path).mkdir(parents=True, exist_ok=True)
            filename = str(Path(path) / "TMDB.log")
            ch2 = TimedRotatingFileHandler(filename, when='h', interval=1)
            ch2.setFormatter(tmdbapi.LOG_FORMATTER)
            ch2.namer = lambda name: name.replace(".log", "") + ".log"
            tmdbapi.LOGGER.addHandler(ch2)
        else:
            tmdbapi.LOGGER.handlers.pop()
    if (kwargs.get("use_access_token")
        and tmdbapi.credential.CREDENTIALS["access_token"] is None):
        del kwargs["use_access_token"]
        tmdbapi.LOGGER.warning("access_token does not exist, use_access_token remain False.")
    SETTINGS.update(kwargs)
    change = dict(set(pre_setting.items()) ^ set(SETTINGS.items()))
    if change:
        change_str = ", ".join(change)
        tmdbapi.LOGGER.info(f"Settings update: {change_str}")


def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning
            an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")