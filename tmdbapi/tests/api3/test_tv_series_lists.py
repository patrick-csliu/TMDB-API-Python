import sys

import tmdbapi


def setup_module():
    loaded_package_modules = [
        key for key, value in sys.modules.items() if "tmdbapi" in str(value)
    ]
    for key in loaded_package_modules:
        del sys.modules[key]
    global tmdbapi  # reach the global scope
    import tmdbapi  # reimport package every before test

    cred = tmdbapi.Credential()
    cred.load("tmdbapi/tests/temp/test.credential")
    tmdbapi.setting.use_cred(cred)


LANGUAGE = "en-US"
TIMEZONE = "Asia/Taipei"


def test_airing_today():
    tmdbapi.api3.tv_series_lists.airing_today(language=LANGUAGE, timezone=TIMEZONE)


def test_on_the_air():
    tmdbapi.api3.tv_series_lists.on_the_air(language=LANGUAGE, timezone=TIMEZONE)


def test_popular():
    tmdbapi.api3.tv_series_lists.popular(language=LANGUAGE)


def test_top_rated():
    tmdbapi.api3.tv_series_lists.top_rated(language=LANGUAGE)
