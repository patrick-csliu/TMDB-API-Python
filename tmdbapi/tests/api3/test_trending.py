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


TEST1 = ["week", "zh-TW"]
TEST2 = ["day", "en-US"]


def test_all():
    tmdbapi.api3.trending.all(*TEST1)


def test_movies():
    tmdbapi.api3.trending.movies(*TEST1)


def test_people():
    tmdbapi.api3.trending.people(*TEST2)


def test_tv():
    tmdbapi.api3.trending.tv(*TEST1)
