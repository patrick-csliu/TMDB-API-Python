"""A TMDB API Library


"""

import importlib as _importlib

from ._core import use_access_token
from .credential import load_credentials, save_credentials, set_credentials

_submodules = ['api3', 'api4', 'tests', 'credential', 'exceptions']
__all__ = _submodules + ['use_access_token', 'load_credentials', 'save_credentials', 'set_credentials']


def __getattr__(name):
    if name in _submodules:
        return _importlib.import_module(f'tmdbapi.{name}')
    else:
        raise AttributeError(
            f"Package 'tmdbapi' has no attribute '{name}'"
        )
