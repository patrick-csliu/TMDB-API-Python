"""A TMDB API Library


"""

import importlib as _importlib
import logging as _logging

from . import api3, api4
from ._core import settings
from .credential import load_credentials, save_credentials, set_credentials

_submodules = ['api3', 'api4', 'tests', 'credential', 'exceptions']
__all__ = _submodules + ['settings', 'load_credentials', 'save_credentials', 'set_credentials']


LOGGER = _logging.getLogger("TMDB")
LOG_FORMATTER = _logging.Formatter("%(asctime)s [%(name)s] [%(levelname)s] - %(message)s")
if not any(isinstance(x, _logging.StreamHandler) for x in LOGGER.handlers):
    _ch1 = _logging.StreamHandler()
    _ch1.setFormatter(LOG_FORMATTER)
    LOGGER.addHandler(_ch1)
    LOGGER.setLevel(_logging.INFO)


def __getattr__(name):
    if name in _submodules:
        return _importlib.import_module(f'tmdbapi.{name}')
    else:
        raise AttributeError(
            f"Package 'tmdbapi' has no attribute '{name}'"
        )
