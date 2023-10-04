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


TEST = ["en-US", "TW", 2]


def test_now_playing():
    tmdbapi.api3.movie_lists.now_playing(*TEST)


def test_popular():
    tmdbapi.api3.movie_lists.popular(*TEST)


def test_top_rated():
    tmdbapi.api3.movie_lists.top_rated(*TEST)


def test_upcoming():
    tmdbapi.api3.movie_lists.upcoming(*TEST)
