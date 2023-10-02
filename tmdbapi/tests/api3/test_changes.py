import sys

import tmdbapi


def setup_module():
    loaded_package_modules = [key for key, value in sys.modules.items() if "tmdbapi" in str(value)]
    for key in loaded_package_modules:
        del sys.modules[key]
    global tmdbapi  # reach the global scope
    import tmdbapi  # reimport package every before test
    tmdbapi.load_credentials("tmdbapi/tests/temp/test.credential")

TEST = ["2023-07-23", "2023-07-27", 3] # [start_date, end_date, page]


def test_movie_list():
    tmdbapi.api3.changes.movie_list(*TEST)


def test_person_list():
    tmdbapi.api3.changes.person_list(*TEST)


def test_tv_list():
    tmdbapi.api3.changes.tv_list(*TEST)
