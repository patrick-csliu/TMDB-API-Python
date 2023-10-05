"""Manage TMDB Credentials

Provides functions for setting, saving, loading, and managing TMDB API
credentials, including access tokens, API keys, session IDs, account 
IDs, and account object IDs.
"""

import os
import pickle
from pathlib import Path

import tmdbapi


class Credential:
    """Manage API credentials.

    This class is used to manage API credentials, including access tokens,
    API keys, session IDs, account IDs, and account object IDs. It provides
    methods for setting, loading, and saving credentials to a file, as well
    as setting credentials as environment variables.

    Attributes
    ----------
    filepath : str
        The file path where the credentials will be saved or loaded from.
    file_update : bool
        A flag indicating whether to automatically update the credentials
        file when credentials are modified.

    Methods
    -------
    set(access_token="", api_key="", session_id="", account_id=0,
        account_object_id="", overwrite=False):
        Set API credentials.

    save(filepath="", auto_update=True):
        Save the credentials to a file.

    load(filepath, auto_update=True):
        Load the credentials from a file.

    cred_to_env():
        Set credentials as environment variables.

    load_env_var(customize_var_names={}):
        Load credentials from environment variables.

    pass_check(*args):
        Check if the specified credentials are present and valid.

    pprint():
        Pretty print the credential dictionary.

    """

    def __init__(self):
        self._cred = {
            "access_token": "",
            "api_key": "",
            "session_id": "",
            "account_id": 0,
            "account_object_id": "",
        }
        self.filepath = ""
        self.file_update = True

    def __getitem__(self, key):
        return self._cred[key]

    def __repr__(self):
        return repr(self._cred)

    def __str__(self):
        return str(self._cred)

    def __eq__(self, other):
        return self._cred == other

    def __ne__(self, other):
        return self._cred != other

    def pprint(self):
        tmdbapi.pprint(self._cred)

    def _set(self, cred, save: bool):
        pre_cred = self._cred.copy()
        self._cred = cred
        # compare the difference and write the change in log.
        change = dict(set(pre_cred.items()) ^ set(self._cred.items()))
        if change:
            change_str = ", ".join(change)
            tmdbapi.LOGGER.info(f"Credential update: {change_str}")
        # save the changes.
        if save:
            if self.filepath != "" and self.file_update:
                self.save(auto_update=self.file_update)
        # if access_token given then use access_token instead of api_key
        if tmdbapi.setting["credential"] is not None:
            if self._cred["access_token"] == "":
                tmdbapi.setting.set(use_access_token=False)
            else:
                tmdbapi.setting.set(use_access_token=True)

    def set(
        self,
        access_token: str = "",
        api_key: str = "",
        session_id: str = "",
        account_id: int = 0,
        account_object_id: str = "",
        overwrite=False,
    ):
        """Set API credentials.

        This method allows you to set or update the API credentials. You can provide an
        access token, an API key, a session ID, an account ID, and an account object ID.
        If you provide an access token, it will be used as the access token in API
        version 3 (api3) by default.
        To change the API key used, you can use `tmdbapi.setting(use_access_token=False)`.

        Parameters
        ----------
        access_token : str, optional
            The Bearer token. If provided, it will be used as the access token
            in API version 3 (api3) by default. To change the API key, use
            `tmdbapi.setting(use_access_token=False)`.
        api_key : str, optional
            The API key for TMDB API version 3. If an access_token is provided,
            there is no need for an api_key. For more information, see:
            https://developer.themoviedb.org/docs/authentication-application.
        session_id : str, optional
            An ID granting permission to access resources.
        account_id : int, optional
            The TMDB API version 3 account ID.
        account_object_id : str, optional
            The TMDB API version 4 account ID.
        overwrite : bool, optional
            If True, the provided credentials will completely replace the
            existing credentials. If False (default), the provided credentials
            will be merged with the existing credentials, updating only the
            non-empty fields.

        Notes
        -----
        After setting the credentials, you can use `save()` to persist them to a file.

        """
        if overwrite:
            cred = {}
            cred["access_token"] = access_token
            cred["api_key"] = api_key
            cred["session_id"] = session_id
            cred["account_id"] = account_id
            cred["account_object_id"] = account_object_id
        else:
            cred = self._cred.copy()
            if access_token != "":
                cred["access_token"] = access_token
            if api_key != "":
                cred["api_key"] = api_key
            if session_id != "":
                cred["session_id"] = session_id
            if account_id != 0:
                cred["account_id"] = account_id
            if account_object_id != "":
                cred["account_object_id"] = account_object_id
        self._set(cred, True)

    def save(self, filepath: str = "", auto_update=True):
        """Save the credentials to a file.

        This method allows you to save the API credentials to a file. It's
        important to note that the file is not encrypted, so it should be
        placed in a secure location to prevent unauthorized access.

        Parameters
        ----------
        filepath : str, optional
            The file path where the credentials will be saved. If not specified,
            it will use the file path loaded or saved previously.
        auto_update : bool, optional
            A flag indicating whether to automatically update the credentials
            file when credentials are modified (default is True).

        Notes
        -----
        This method will save the credentials stored in the `Credential` instance
        to the specified file path. If `filepath` is not provided, it will use
        the file path that was previously loaded or saved. If the file does not
        exist, it will be created. Any existing file at the specified location
        will be overwritten.

        """
        path_given = filepath != ""
        path_exist = self.filepath != ""
        if path_given:
            self.filepath = filepath
        else:
            if path_exist:
                filepath = self.filepath
            else:
                raise ValueError(
                    "No filepath provided. Please specify a valid file path to save the credentials."
                )
        self.file_update = auto_update
        path = Path(filepath)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, "wb") as f:
            pickle.dump(self._cred, f)
        tmdbapi.LOGGER.info(f"Credential store at {path.absolute()}")

    def load(self, filepath: str, auto_update=True):
        """Load the credentials from a file.

        This method allows you to load API credentials from a specified file.
        The previous credential information stored in the `Credential` instance
        will be discarded, and the new credentials from the file will be used.

        Parameters
        ----------
        filepath : str
            The file path where the credentials will be loaded from.
        auto_update : bool, optional
            A flag indicating whether to automatically update the credentials
            file when credentials are modified (default is True).

        Notes
        -----
        The credentials file must be in a specific format created by the `save()`
        method, and it cannot be customized. The file format includes fields for
        "access_token," "api_key," "session_id," "account_id," and
        "account_object_id." If the file format does not match, an exception
        will be raised.

        """
        with open(filepath, "rb") as f:
            temp = pickle.load(f)
        # type checking
        if isinstance(temp, dict) and set(temp.keys()) == {
            "access_token",
            "api_key",
            "session_id",
            "account_id",
            "account_object_id",
        }:
            tmdbapi.LOGGER.info("Credentials loaded successfully.")
            self._set(temp, False)
        else:
            raise Exception(
                "The credential file format is invalid. Please ensure that the file was created using the 'save()' method and follows the required format."
            )
        self.file_update = auto_update
        self.filepath = filepath

    def cred_to_env(self):
        """Set credentials as environment variables.

        This method sets the API credentials stored in the `Credential` instance
        as environment variables. Each credential field is mapped to a specific
        environment variable name:

        - "access_token" is mapped to "TMDB_ACCESS_TOKEN"
        - "api_key" is mapped to "TMDB_API_KEY"
        - "session_id" is mapped to "TMDB_SESSION_ID"
        - "account_id" is mapped to "TMDB_ACCOUNT_ID"
        - "account_object_id" is mapped to "TMDB_ACCOUNT_OBJECT_ID"

        The credentials are converted to strings before being set as environment
        variables.

        Notes
        -----
        Setting credentials as environment variables can be useful when you want
        to use them in other parts of your code that rely on environment variables
        for configuration.

        """
        cred_env = {}
        var_names = {
            "access_token": "TMDB_ACCESS_TOKEN",
            "api_key": "TMDB_API_KEY",
            "session_id": "TMDB_SESSION_ID",
            "account_id": "TMDB_ACCOUNT_ID",
            "account_object_id": "TMDB_ACCOUNT_OBJECT_ID",
        }
        for k, v in self._cred.items():
            name_env = var_names[k]
            cred_env[name_env] = str(v)
        os.environ.update(cred_env)
        tmdbapi.LOGGER.info(
            "API credentials successfully set as environment variables."
        )

    def load_env_var(self, customize_var_names={}):
        """Load credentials from environment variables.

        This method allows you to load API credentials from environment variables.
        The previous credential information stored in the `Credential` instance will
        be discarded, and the new credentials from environment variables will be used.

        Note: This function will clear previous credentials. To save the current
        credentials, use the `save()` method before calling this function.

        Parameters
        ----------
        customize_var_names : dict, optional
            A dictionary that maps credential variable names to their corresponding
            environment variable names if they are different from the defaults.
            Default:

            .. code-block:: python

                {
                    "access_token": "TMDB_ACCESS_TOKEN",
                    "api_key": "TMDB_API_KEY",
                    "session_id": "TMDB_SESSION_ID",
                    "account_id": "TMDB_ACCOUNT_ID",
                    "account_object_id": "TMDB_ACCOUNT_OBJECT_ID",
                }

            You cannot change the keys in this dictionary.

        Notes
        -----
        This method retrieves credentials from environment variables based on the
        specified or default variable names and sets them in the `Credential`
        instance.

        """
        var_names = {
            "access_token": "TMDB_ACCESS_TOKEN",
            "api_key": "TMDB_API_KEY",
            "session_id": "TMDB_SESSION_ID",
            "account_id": "TMDB_ACCOUNT_ID",
            "account_object_id": "TMDB_ACCOUNT_OBJECT_ID",
        }
        var_names.update(customize_var_names)
        cred = {}
        for k, v in var_names.items():
            cred[k] = os.environ.get(v, "")
        if cred.get("account_id") != "":
            cred["account_id"] = int(cred["account_id"])
        tmdbapi.LOGGER.info(
            "API credentials loaded successfully from environment variables."
        )
        self._set(cred, True)

    def pass_check(self, *args):
        """Check if specified credentials are present and valid.

        Returns True if all specified credentials are non-empty and valid.
        Otherwise, returns False.

        Parameters
        ----------
        *args : str
            Variable names to check for validity.

        """
        for key in args:
            if key != "account_id":
                if self._cred[key] == "":
                    return False
            else:
                if self._cred[key] == 0:
                    return False
        return True
