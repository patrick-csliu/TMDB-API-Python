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
    def __init__(self):
        self.cred = {
            "access_token": "",
            "api_key": "",
            "session_id": "",
            "account_id": None,
            "account_object_id": "",
        }
        self.filepath = ""
        self.file_update = True
    
    def __getitem__(self, key):
        return self.cred[key]
    
    # def __setitem__(self, key, value):
    #     self.cred[key] = value

    def __repr__(self):
        return repr(self.cred)
    
    def __str__(self):
        return str(self.cred)
    
    def __eq__(self, other):
        return self.cred == other
    
    def __ne__(self, other):
        return self.cred != other
    
    def pprint(self):
        tmdbapi.pprint(self.cred)

    def set(self, access_token: str = "", api_key: str = "",
            session_id: str = "", account_id: int = 0,
            account_object_id: str = "", overwrite=False):
        """Set API credentials.

        This function stores the provided credentials in module global 
        variables. To persist the credentials in a file, use 
        `save_credentials()` after loading them.

        Parameters
        ----------
        access_token : str, optional
            The Bearer token. If provided, it will be used as the access 
            token in API version 3 (api3) by default. To change the API key
            , use `settings(use_access_token=False)`.
        api_key : str, optional
            The API key for TMDB API version 3. If an access_token is provided, 
            there is no need for an api_key. For more information, 
            see: https://developer.themoviedb.org/docs/authentication-application.
        session_id : str, optional
            An ID granting permission to access resources.
        account_id : int, optional
            The TMDB API version 3 account ID.
        account_object_id : str, optional
            The TMDB API version 4 account ID.
        """
        pre_cred = self.cred.copy()
        if overwrite:
            self.cred["access_token"] = access_token
            self.cred["api_key"] = api_key
            self.cred["session_id"] = session_id
            self.cred["account_id"] = account_id
            self.cred["account_object_id"] = account_object_id
        else:
            if access_token != "":
                self.cred["access_token"] = access_token
            if api_key != "":
                self.cred["api_key"] = api_key
            if session_id != "":
                self.cred["session_id"] = session_id
            if account_id != 0:
                self.cred["account_id"] = account_id
            if account_object_id != "":
                self.cred["account_object_id"] = account_object_id
        # compare the difference and write the change in log.
        change = dict(set(pre_cred.items()) ^ set(self.cred.items()))
        if change:
            change_str = ", ".join(change)
            tmdbapi.LOGGER.info(f"Credential update: {change_str}")
        # save the change.
        if self.filepath != "" and self.file_update:
            self.save(auto_update=self.file_update)
        # if access_token given then use access_token instead of api_key
        if tmdbapi.setting["credential"] is not None:
            if self.cred["access_token"] == "":
                tmdbapi.setting.set(use_access_token=False)
            else:
                tmdbapi.setting.set(use_access_token=True)

    def save(self, filepath: str = "", auto_update=True):
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
        path_given = filepath != ""
        path_exist = self.filepath != ""
        if path_given:
            self.filepath = filepath
        else:
            if path_exist:
                filepath = self.filepath
            else:
                raise ValueError("No filepath given.")
        self.file_update = auto_update
        path = Path(filepath)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'wb') as f:
            pickle.dump(self.cred, f)
        tmdbapi.LOGGER.info(f"Credential store at {path.absolute()}")

    def load(self, filepath: str, auto_update=True):
        """Load the credentials from file.

        The previous credential information will be discard, and use the new one.
        The format cannot be customized and can only be loaded from a file
        created by `save_credentials()`.

        Parameters
        ----------
        filepath : str
            The file path where the credentials will be loaded from.
        """
        with open(filepath, 'rb') as f:
            temp = pickle.load(f)
        # type checking
        if (isinstance(temp, dict)
            and set(temp.keys()) == {"access_token", "api_key", "session_id",
                                     "account_id", "account_object_id"}):
            self.set(**temp, overwrite=True)
        else:
            raise Exception("The credential file is invalid.")
        tmdbapi.LOGGER.info(f"Credential loaded successful.")
        self.file_update = auto_update
        self.filepath = filepath

    def cred_to_env(self):
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
        for k, v in self.cred.items():
            name_env = var_names[k]
            cred_env[name_env] = str(v)
        os.environ.update(cred_env)
        tmdbapi.LOGGER.info(f"Set credentials as environment variables.")

    def load_env_var(self, customize_var_names={}):
        """Load credentials from environment variables.

        The previous credential information will be discard, and use the new one.
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
        tmdbapi.LOGGER.info(f"Load credentials from environment variables.")
        self.set(**cred, overwrite=True)
    
    def pass_check(self, *args):
        for key in args:
            if key != "account_id":
                if self.cred[key] == "":
                    return False
            else:
                if self.cred[key] == 0:
                    return False
        return True



# def credential_check(needed: str) -> bool:
#     """Check if the needed credentials exist.

#     Parameters
#     ----------
#     needed : str
#         valid values:
#         'access_token', 'api_key', 'session_id', 'account_object_id'

#     Returns
#     -------
#     bool
#         Return True if the needed credential exist.

#     Raises
#     ------
#     ExceptionGroup
#         If the needed credentials do not exist.
#     """
#     token_type = (
#         "access_token",
#         "api_key",
#         "session_id",
#         "account_object_id"
#     )
#     token_exist = [tmdbapi.creds.CREDENTIALS[token] is not None for token in token_type]
#     exceptions = [
#         Exception("You must set up an access token before making this request. Please configure your access token settings to proceed."),
#         Exception("You must set up an api_key before making this request. Please configure your api_key settings to proceed."),
#         Exception("You must set up an session_id before making this request. Please configure your session_id settings to proceed."),
#         Exception("You must set up an account_object_id before making this request. Please configure your account_object_id settings to proceed."),
#     ]
#     errors = []
#     for i in range(4):
#         if token_type[i] in needed and not token_exist[i]:
#             errors.append(exceptions[i])
#     if len(errors) != 0:
#         raise ExceptionGroup("Missing credential", errors)
#     else:
#         return True