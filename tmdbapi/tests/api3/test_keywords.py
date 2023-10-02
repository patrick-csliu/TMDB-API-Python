import sys

import tmdbapi


def setup_module():
    loaded_package_modules = [key for key, value in sys.modules.items() if "tmdbapi" in str(value)]
    for key in loaded_package_modules:
        del sys.modules[key]
    global tmdbapi  # reach the global scope
    import tmdbapi  # reimport package every before test
    tmdbapi.load_credentials("tmdbapi/tests/temp/test.credential")



def test_details():
    tmdbapi.api3.keywords.details(271668)


def test_movies():
    tmdbapi.api3.keywords.movies(271668, "zh-TW")
