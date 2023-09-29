"""
The core of the tmdb request api
"""

import requests

from .credential import CREDENTIALS
from .exceptions import TmdbApiException
from typing import TypedDict, Optional

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

SETTINGS: SettingsType = {
        # "tmdb_cache_enable": True,
        "use_access_token": False,
        "timeout": None,
        "default_language": None,
        "default_region": None,
        "use_session": False
}

class Tmdb:

    _headers = {"accept": "application/json",}
    session = requests.Session()
    base_path = ""  # The base path for each api category
    info_var: dict = None # The information dictionary for each api category
                    # Information dictionary contains http request 
                    # method, path and parameters for each service. 

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
    
    def _authentication(self, headers: dict, params: dict) -> tuple[dict, dict]:
        """Set the headers and query(params) by 'use_access_token' setting

        Parameters
        ----------
        headers : dict
        params : dict

        Returns
        -------
        tuple[dict, dict]
            (headers, query)
        """
        if SETTINGS["use_access_token"]:
            token = CREDENTIALS["access_token"]
            headers["Authorization"] = f"Bearer {token}"
        else:
            params["api_key"] = CREDENTIALS["api_key"]
        return headers, params

    def check_token(self) -> dict:
        """Check now is using access_token or api_key

        If access_token used, no needed for session_id.

        Returns
        -------
        dict
            A dict for query.
        """
        if SETTINGS["use_access_token"]:
            return {}
        else:
            return {"session_id": CREDENTIALS["session_id"]}

    def choose_session_id(self, guest_session_id: str):
        """Choose a session_id

        If `guest_session_id` is provided use `guest_session_id`;
        otherwise, use `session_id`.

        Parameters
        ----------
        guest_session_id : str
        """
        if guest_session_id is None:
            self._query.update(self.check_token())
        else:
            self._query.update(guest_session_id=guest_session_id)

    def use(self, name: str):
        """Select a service from information dict

        Parameters
        ----------
        name : str
            key in the dict
        """
        self._ref = self.info_var[name]["url"]
        self._method = self.info_var[name]["method"]
        self._name = name

    def load_query(self, query={}, **kwargs):
        """Update the query parameters

        Parameters
        ----------
        query : dict, optional
        """
        self._query.update(query)
        self._query.update(kwargs)

    def load_path_arg(self, args={}, **kwargs):
        """Update the parameters in the _rel

        Example: The account.details have the rel = "/{account_id}/favorite"
        And therefor it has one parameter `account_id`.
        This is assign by load_path_arg(account_id=xxx).

        Parameters
        ----------
        args : dict, optional
        """
        self._path_args.update(args)
        self._path_args.update(kwargs)

    def load_json(self, json_dict: dict):
        """Give the dict format payload

        Parameters
        ----------
        json_dict : dict
        """
        self._json = json_dict

    def build_url(self, version: int) -> str:
        """Build the url for request

        Parameters
        ----------
        version : int
            3 or 4

        Returns
        -------
        str
            the url without query
        """
        self._ref = self._ref.format(**self._path_args)
        return f"{API_BASE}/{version}{self.base_path}{self._ref}"

    def sortby(self, asc: bool):
        """Update query by the api sort_by valid values

        Parameters
        ----------
        asc : bool
            True : ascending
            False: descending
        """
        if asc:
            s =  {"sort_by": "created_at.asc"}
        else:
            s =  {"sort_by": "created_at.desc"}
        self._query.update(s)
    
    def language(self, lang: str = None):
        """Update the language parameter to query

        Use default language setting except the lang given.

        Parameters
        ----------
        lang : str, optional
            format: `language-COUNTRY`
            example: 'zh-TW', 'en-US'
            see: https://developer.themoviedb.org/docs/languages
        """
        if lang is not None:
            s = {"language": lang}
        elif SETTINGS["default_language"] is not None:
            s = {"language": SETTINGS["default_language"]}
        else:
            s = {}
        self._query.update(s)

    def region(self, region: str = None):
        """Update the region parameter to query

        Parameters
        ----------
        region : str, optional
            format: ISO 3166-1
        """
        if region is not None:
            s = {"region": region}
        elif SETTINGS["default_language"] is not None:
            s = {"region": SETTINGS["default_region"]}
        else:
            s = {}
        self._query.update(s)

    def reset(self):
        """Clean all content in variables
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
            The dictionary from function input

        Returns
        -------
        bool
            Return True if pass the check, otherwise return false.
        """
        params_name = []
        for p in self.info_var[self._name]["params"]:
            params_name.append(p["name"])
        return set(params.keys()).issubset(set(params_name))

    def request_raw(self, url: str, method: str = None, params: dict = None, data=None, json: dict = None) -> dict:
        """Send the request and handle the return

        Parameters
        ----------
        url : str
            url without query
        method : str, optional
            request method, by default None
        params : dict, optional
            query for url, by default None
        data : _type_, optional
            The payload, by default None
        json : dict, optional
            The payload, by default None

        Returns
        -------
        dict
            json format

        Raises
        ------
        TmdbApiException
            If the action not success
        """
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
        
        print("json:", json)
        print(method, headers)
        # request from api
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

        print(response.url)
        headers = response.headers

        header_status_code = response.status_code
        has_content = headers.get("content-length", "1") != "0"
        if has_content:
            if headers.get("Content-Type", "").startswith("application/json"):
                content =  response.json()
            else:
                TmdbApiException(f"status_code: {header_status_code}",
                                 "The content is not json. Content:",
                                 response.content)
                content = response.content
        else:
            TmdbApiException(f"status_code: {header_status_code}",
                             "No content.")
        print(f"status_code: {header_status_code}")
        is_success = content.get("success", None)
        if is_success is not None and is_success == False:
            raise TmdbApiException(content["status_message"])
        else:
            return content


def use_access_token(use: bool):
    """Use access_token or not

    Parameters
    ----------
    use : bool
        True: Use the access_token
        False: Use the api_key
    """
    if use and credential_check(("access_token")):
        SETTINGS["use_access_token"] = True
    else:
        SETTINGS["use_access_token"] = False


def credential_check(needed: str) -> bool:
    """Check the needed credential exist

    Parameters
    ----------
    needed : str
        valid values:
        'access_token', 'api_key', 'session_id', 'account_object_id'

    Returns
    -------
    bool
        Return True if the needed credential exist

    Raises
    ------
    ExceptionGroup
        If the needed credential is not exist
    """
    token_type = (
        "access_token",
        "api_key",
        "session_id",
        "account_object_id"
    )
    token_exist = [CREDENTIALS[token] is not None for token in token_type]
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
        "use_session": False
    }
    ```
    Raises
    ------
    ValueError
        If the setting not in the Settings options
    """
    if not set(kwargs.keys()).issubset(SETTINGS.keys()):
        raise ValueError("The setting you given if not the options")
    if "use_session" in kwargs.keys() and kwargs["use_session"] != SETTINGS["use_session"]:
        if kwargs["use_session"]:
            Tmdb.session = requests.Session()
        else:
            Tmdb.session = None
    SETTINGS.update(kwargs)
        