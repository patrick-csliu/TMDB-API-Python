"""A TMDB API Library

A comprehensive Python library for interacting with TheMovieDB API, 
supporting both version 3 and version 4.
This package includes subpackages, modules, and utilities for seamless 
access to the TMDB API.

Subpackages
-----------
- `api3`: TMDB API version 3 methods and endpoints.
- `api4`: TMDB API version 4 methods and endpoints.
- `integration`: High-level functions and integration features for simplifying 
interactions with TMDB.
- `tests`: Contains unit tests using pytest.

Modules
-------
- `creds.py`: Manages credentials for API access.
- `exceptions.py`: Contains custom exception and warning classes.
- `_core.py`: The main part of the TMDB request class and the Setting class 
for API configuration.

Documentation
-------------
Documentation is available through docstrings provided with the code,
and can also be accessed on the <https://github.com/patrick-csliu/TMDB-API-Python>.

Getting Started
---------------
To begin using the library, start by loading your credentials:

    >>> import tmdbapi
    >>> cred = tmdbapi.Credential()
    >>> cred.set(api_key="your_api_key",
    ...          access_token="your_access_token",
    ...          account_object_id="your_account_object_id")
    >>> tmdbapi.setting.use_cred(cred)

License:
This package is distributed under the MIT License.

"""

import importlib as _importlib
import logging as _logging

LOGGER = _logging.getLogger("TMDB")
LOG_FORMATTER = _logging.Formatter(
    "%(asctime)s [%(name)s] [%(levelname)s] - %(message)s"
)
if not any(isinstance(x, _logging.StreamHandler) for x in LOGGER.handlers):
    _ch1 = _logging.StreamHandler()
    _ch1.setFormatter(LOG_FORMATTER)
    LOGGER.addHandler(_ch1)
    LOGGER.setLevel(_logging.INFO)


from ._core import Setting as _Setting
from ._core import pprint

setting = _Setting()


from . import api3, api4, integration
from .creds import Credential

_submodules = ["api3", "api4", "integration", "tests", "cred", "exceptions"]
__all__ = _submodules + ["Setting", "Credential", "pprint"]


_SESSION = None  # requests.Session


def __getattr__(name):
    if name in _submodules:
        return _importlib.import_module(f"tmdbapi.{name}")
    else:
        raise AttributeError(f'Package "tmdbapi" has no attribute "{name}"')
