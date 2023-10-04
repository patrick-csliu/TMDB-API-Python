"""API v3 configuration category

"""

from tmdbapi._core import Tmdb

_CONFIGURATION_V3 = {
    "configuration-countries": {
        "method": "get",
        "params": [{"in": "query", "name": "language"}],
        "url": "/countries",
    },
    "configuration-details": {"method": "get", "params": [], "url": ""},
    "configuration-jobs": {
        "method": "get",
        "params": [],
        "url": "/jobs",
    },
    "configuration-languages": {
        "method": "get",
        "params": [],
        "url": "/languages",
    },
    "configuration-primary-translations": {
        "method": "get",
        "params": [],
        "url": "/primary_translations",
    },
    "configuration-timezones": {
        "method": "get",
        "params": [],
        "url": "/timezones",
    },
}


class _Configuration(Tmdb):
    def __init__(self, info_var):
        super().__init__()
        self.category_path = "/configuration"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url=url,
        )


def details() -> dict:
    """Query the API configuration details."""
    configuration = _Configuration(_CONFIGURATION_V3)
    configuration.reset()
    configuration.use("configuration-details")
    return configuration.request()


def countries(language: str = None) -> dict:
    """Get the list of countries (ISO 3166-1 tags) used throughout
    TMDB.
    """
    configuration = _Configuration(_CONFIGURATION_V3)
    configuration.reset()
    configuration.use("configuration-countries")
    configuration.language(language)
    return configuration.request()


def jobs() -> dict:
    """Get the list of the jobs and departments we use on TMDB."""
    configuration = _Configuration(_CONFIGURATION_V3)
    configuration.reset()
    configuration.use("configuration-jobs")
    return configuration.request()


def languages() -> dict:
    """Get the list of languages (ISO 639-1 tags) used throughout TMDB."""
    configuration = _Configuration(_CONFIGURATION_V3)
    configuration.reset()
    configuration.use("configuration-languages")
    return configuration.request()


def primary_translations() -> dict:
    """Get a list of the officially supported translations on TMDB."""
    configuration = _Configuration(_CONFIGURATION_V3)
    configuration.reset()
    configuration.use("configuration-primary-translations")
    return configuration.request()


def timezones() -> dict:
    """Get the list of timezones used throughout TMDB."""
    configuration = _Configuration(_CONFIGURATION_V3)
    configuration.reset()
    configuration.use("configuration-timezones")
    return configuration.request()
