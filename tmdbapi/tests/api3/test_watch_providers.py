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


TEST = ["zh-TW", "TW"]


def test_available_regions():
    tmdbapi.api3.watch_providers.available_regions(TEST[0])


def test_movie_providers():
    tmdbapi.api3.watch_providers.movie_providers(*TEST)


def test_tv_providers():
    tmdbapi.api3.watch_providers.tv_providers(*TEST)
