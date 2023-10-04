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


# def teardown_module():
#     """ teardown any state that was previously setup with a setup_module
#     method."""
#     loaded_package_modules = [key for key, value in sys.modules.items() if "tmdbapi" in str(value)]
#     for key in loaded_package_modules:
#         del sys.modules[key]


MOVIE = [278, "movie"]  # [media_id, media_type]
TV = [1396, "tv"]  # [media_id, media_type]
LANGUAGE = "zh-TW"


def test_details():
    tmdbapi.api3.account.details()


class TestFavorite:
    def test_add_movie(self):
        print(tmdbapi.api3.account.add_favorite(MOVIE[0], MOVIE[1]))

    def test_add_tv(self):
        print(tmdbapi.api3.account.add_favorite(TV[0], TV[1]))

    def test_get_movie(self):
        print(tmdbapi.api3.account.favorite_movies(asc_sort=False, language=LANGUAGE))

    def test_get_tv(self):
        print(tmdbapi.api3.account.favorite_tv_shows(asc_sort=False, language=LANGUAGE))

    def test_remove_movie(self):
        print(tmdbapi.api3.account.add_favorite(MOVIE[0], MOVIE[1], False))

    def test_remove_tv(self):
        print(tmdbapi.api3.account.add_favorite(TV[0], TV[1], False))


class TestWatchlist:
    def test_add_movie(self):
        print(tmdbapi.api3.account.add_to_watchlist(MOVIE[0], MOVIE[1]))

    def test_add_tv(self):
        print(tmdbapi.api3.account.add_to_watchlist(TV[0], TV[1]))

    def test_get_movie(self):
        print(tmdbapi.api3.account.movie_watchlist(asc_sort=False, language=LANGUAGE))

    def test_get_tv(self):
        print(tmdbapi.api3.account.tv_show_watchlist(asc_sort=False, language=LANGUAGE))

    def test_remove_movie(self):
        print(tmdbapi.api3.account.add_to_watchlist(MOVIE[0], MOVIE[1], False))

    def test_remove_yb(self):
        print(tmdbapi.api3.account.add_to_watchlist(TV[0], TV[1], False))


def test_get_list():
    print(tmdbapi.api3.account.get_list())


def test_rated_movies():
    print(tmdbapi.api3.account.rated_movies(asc_sort=False, language=LANGUAGE))


def test_rated_tv_episodes():
    print(tmdbapi.api3.account.rated_tv_episodes(asc_sort=True, language=LANGUAGE))


def test_rated_tv_shows():
    print(tmdbapi.api3.account.rated_tv_shows(asc_sort=True, language=LANGUAGE))


def test_add_favorite_error():
    with pytest.raises(ValueError):
        tmdbapi.api3.account.add_favorite(MOVIE[0], "apple")


def test_add_to_watchlist_error():
    with pytest.raises(ValueError):
        tmdbapi.api3.account.add_to_watchlist(MOVIE[0], "apple")
