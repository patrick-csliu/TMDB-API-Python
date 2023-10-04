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


class TestMovies:
    def test_param_error(self):
        with pytest.raises(KeyError):
            tmdbapi.api3.discover.movies(
                wrong_name="True",
                include_adult=False,
                include_video=False,
                language="en-US",
                page=1,
                primary_release_year=2016,
                region="TW",
                sort_by="vote_average.asc",
            )

    def test_1(self):
        tmdbapi.api3.discover.movies(
            {"vote_average.gte": 3, "vote_average.lte": 5},
            include_adult=False,
            include_video=False,
            language="en-US",
            page=1,
            primary_release_year=2016,
            region="TW",
            sort_by="vote_average.asc",
        )


class TestTv:
    def test_param_error(self):
        with pytest.raises(KeyError):
            tmdbapi.api3.discover.tv(
                wrong_name="True",
                include_adult=False,
                include_video=False,
                language="en-US",
                page=1,
                primary_release_year=2016,
                region="TW",
                sort_by="vote_average.asc",
            )

    def test_1(self):
        tmdbapi.api3.discover.tv(
            {"vote_average.gte": 3, "vote_average.lte": 5},
            include_adult=False,
            language="en-US",
            page=1,
            first_air_date_year=2016,
            sort_by="vote_average.asc",
        )
