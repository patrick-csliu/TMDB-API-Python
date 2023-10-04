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


LANGUAGE = "zh_TW"


def test_movie_list():
    tmdbapi.api3.genres.movie_list(LANGUAGE)


def test_tv_list():
    tmdbapi.api3.genres.tv_list(LANGUAGE)
