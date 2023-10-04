"""A TMDB API Library


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
