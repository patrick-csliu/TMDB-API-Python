import sys

import pytest

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


TEST = ["2023-07-23", "2023-07-27", 3]  # [start_date, end_date, page]


def test_movie_list():
    tmdbapi.api3.changes.movie_list(*TEST)


def test_movie_list2():
    tmdbapi.api3.changes.movie_list()


def test_person_list():
    tmdbapi.api3.changes.person_list(*TEST)


def test_tv_list():
    tmdbapi.api3.changes.tv_list(*TEST)


class TestDataError:
    def test_movie_list_error1(self):
        with pytest.raises(ValueError):
            tmdbapi.api3.changes.movie_list("2023-7-23", "2023-07-27", 3)

    def test_movie_list_error2(self):
        with pytest.raises(ValueError):
            tmdbapi.api3.changes.movie_list("2023-07-1", "2023-07-10", 3)

    def test_movie_list_error3(self):
        with pytest.raises(ValueError):
            tmdbapi.api3.changes.movie_list("202-07-23", "202-07-27", 3)
