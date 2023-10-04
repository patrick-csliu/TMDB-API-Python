"""
The Core of the TMDb Request API
"""

from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
from typing import Optional
import json as Json

import requests

import tmdbapi
from tmdbapi.exceptions import STATUS, TmdbApiException


class Setting:
    """Settings

    ```
    Default settings:
    {
        "use_access_token": False,
        "timeout": None,
        "default_language": None,
        "default_region": None,
        "use_session": False,
        "log_file": None,
        "credential": None,
    }
    ```
    """

    def __init__(self):
        self.setting = {
            "use_access_token": False,
            "timeout": None,
            "default_language": None,
            "default_region": None,
            "use_session": False,
            "log_file": None,
            "credential": None,
        }

    def __getitem__(self, key):
        return self.setting[key]

    def __repr__(self):
        return repr(self.setting)

    def __str__(self):
        return str(self.setting)

    def __eq__(self, other):
        return self.setting == other

    def __ne__(self, other):
        return self.setting != other
    
    def pprint(self):
        pprint(self.setting)

    def _check_cred_exist(self):
        if self.setting["credential"] is None:
            return False
        else:
            return True

    def set(self, **kwargs):
        """Change settings.

        ```
        Default settings:
        {
            "use_access_token": False,
            "timeout": None,
            "default_language": None,
            "default_region": None,
            "use_session": False,
            "log_file": None,
            "credential": None,
        }
        ```
        Raises
        ------
        KeyError
            If the parameter not in the Settings options.
        """
        settings = kwargs.keys()
        if not set(settings).issubset(self.setting.keys()):
            raise KeyError(
                "The setting you have provided is not among the available options."
            )
        if "use_access_token" in settings:
            self.use_access_token(kwargs["use_access_token"])
        if "timeout" in settings:
            self.timeout(kwargs["timeout"])
        if "default_language" in settings:
            self.language(kwargs["default_language"])
        if "default_region" in settings:
            self.region(kwargs["default_region"])
        if "use_session" in settings:
            self.use_session(kwargs["use_session"])
        if "log_file" in settings:
            self.log(kwargs["log_file"])
        if "credential" in settings:
            self.use_cred(kwargs["credential"])

    def use_access_token(self, use: bool):
        if self._check_cred_exist():
            cred = self.setting["credential"]
        else:
            raise Exception("Please setup the credential.")
        if use != self.setting["use_access_token"]:
            if not cred.pass_check("access_token"):
                tmdbapi.LOGGER.warning(
                    "access_token does not exist, use_access_token remain False."
                )
            else:
                self.setting["use_access_token"] = use
                tmdbapi.LOGGER.info(f'Setting: "use_access_token": {use}.')

    def timeout(self, timeout: Optional[float | tuple] = None):
        self.setting["timeout"] = timeout
        tmdbapi.LOGGER.info(f'Setting: "timeout": {timeout}.')

    def language(self, language: Optional[str]):
        self.setting["default_language"] = language
        tmdbapi.LOGGER.info(f'Setting: "default_language": {language}.')

    def region(self, region: Optional[str]):
        self.setting["default_region"] = region
        tmdbapi.LOGGER.info(f'Setting: "default_region": {region}.')

    def use_session(self, use: bool):
        if use != self.setting["use_session"]:
            if use:
                tmdbapi._SESSION = requests.Session()
            else:
                tmdbapi._SESSION = None
            self.setting["use_session"] = use
            tmdbapi.LOGGER.info(f'Setting: "use_session": {use}.')

    def log(self, directory: Optional[str]):
        if directory != self.setting["log_file"]:
            if directory is None:
                tmdbapi.LOGGER.handlers.pop()
                tmdbapi.LOGGER.info(f"Setting: Disable log file.")
            else:
                Path(directory).mkdir(parents=True, exist_ok=True)
                filename = str(Path(directory) / "TMDB.log")
                ch2 = TimedRotatingFileHandler(filename, when="h", interval=1)
                ch2.setFormatter(tmdbapi.LOG_FORMATTER)
                ch2.namer = lambda name: name.replace(".log", "") + ".log"
                tmdbapi.LOGGER.addHandler(ch2)
                tmdbapi.LOGGER.info(f"Setting: Log files at: {directory}.")
            self.setting["log_file"] = directory

    def use_cred(self, credential):
        self.setting["credential"] = credential
        tmdbapi.LOGGER.info(
            f"Setting: Your credentials have been successfully set in the settings."
        )


class Tmdb:
    """The Tmdb class provides a Python interface for making requests to the TMDb (The Movie Database) API.

    Attributes:
        _headers (dict): Default headers for API requests.

        session (requests.Session): A session for making HTTP requests.

        category_path (str): The base path for each API category.

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

    headers = {
        "accept": "application/json",
    }
    api_base = "https://api.themoviedb.org"

    def __init__(self):
        self.category_path = ""  # Relative path for each category.
        self.info_var = None  # Store the information for each category.
        # Relative path for service (service also call api method).
        self._ref: str = ""
        self._method: str = ""  # http(s) request method.
        self._json: dict = None  # Json payload.
        self._query = {}  # Query(parameters) for url.
        self._path_args = {}  # The values to replace the anchor in url.
        if tmdbapi.setting["credential"] is None:
            raise Exception("No credential given.")
        else:
            self._cred = tmdbapi.setting["credential"]

    def _api_auth(self, headers: dict, params: dict) -> tuple[dict, dict]:
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
        if tmdbapi.setting["use_access_token"]:
            token = self._cred["access_token"]
            headers["Authorization"] = f"Bearer {token}"
        else:
            if self._cred.pass_check("api_key"):
                params["api_key"] = self._cred["api_key"]
            else:
                tmdbapi.LOGGER.error("No api_key given, please set the api_key.")
                raise Exception("No api_key given, please set the api_key.")
        return headers, params

    def check_token(self) -> Optional[dict]:
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
        if tmdbapi.setting["use_access_token"]:
            return {}
        else:
            if self._cred.pass_check("session_id"):
                return {"session_id": self._cred["session_id"]}
            else:
                if self._cred.pass_check("access_token"):
                    tmdbapi.settings(use_access_token=True)
                    return self.check_token()
                else:
                    tmdbapi.LOGGER.info("No session_id, creating a session_id.")
                    tmdbapi.integration.auth.create_session_id()
                    return {"session_id": self._cred["session_id"]}

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
        ref = f"{self.category_path}{self._ref}"
        ref = ref.format(**self._path_args)
        return f"{self.api_base}/{version}{ref}"

    def sortby(self, asc: bool):
        """Update the query by specifying ascending or descending sorting order.

        Parameters
        ----------
        asc : bool
            True: Sort in ascending order.
            False: Sort in descending order.
        """
        if asc:
            s = {"sort_by": "created_at.asc"}
        else:
            s = {"sort_by": "created_at.desc"}
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
        elif tmdbapi.setting["default_language"] is not None:
            s = {"language": tmdbapi.setting["default_language"]}
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
        elif tmdbapi.setting["default_language"] is not None:
            s = {"region": tmdbapi.setting["default_region"]}
        else:
            s = {}
        self._query.update(s)

    def reset(self):
        """Reset all content in instance variables."""
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

    def request_raw(
        self,
        url: str,
        method: str = None,
        params: dict = None,
        data=None,
        json: dict = None,
    ) -> dict:
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
        params = {
            k: str(v).lower() if isinstance(v, bool) else v for k, v in params.items()
        }
        if json is None:
            json = self._json
        headers, params = self._api_auth(headers=self.headers.copy(), params=params)
        if json is not None:
            headers["content-type"] = "application/json"

        # debug print #
        print("json:", json)
        print(method, headers)

        # send request to tmdb api
        #
        if tmdbapi.setting["use_session"]:
            request = self.session
        else:
            request = requests
        # if self.cache and method == "GET":
        # response = self.cached_request(method, url, params=params,
        #                                headers=headers)
        # response = request.request(method, url, params=params,
        #                            headers=headers)
        # else:
        response = request.request(
            method,
            url,
            data=data,
            json=json,  # proxies=self.proxies,
            params=params,
            headers=headers,
            timeout=tmdbapi.setting["timeout"],
        )

        headers = response.headers
        header_status_code = response.status_code
        # debug print #
        tmdbapi.LOGGER.info(
            f"status_code: {header_status_code}, {method}: {response.url}"
        )
        # handle response
        has_content = headers.get("content-length", "1") != "0"
        if has_content:
            if headers.get("Content-Type", "").startswith("application/json"):
                content = response.json()
            else:
                content = response.text
                TmdbApiException("The content is not json. Content:", content)
        else:
            TmdbApiException("No content.")
        if isinstance(content, dict):
            is_success = content.get("success", None)
            if is_success is not None and is_success == False:
                raise TmdbApiException(content["status_message"])
        return content


def query_yes_no(question: str, default="yes"):
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
        print(question + prompt, end="")
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            print("Please respond with 'yes' or 'no' " "(or 'y' or 'n').")


def pprint(json, indent=2):
    print(Json.dumps(json, indent=indent))
    
