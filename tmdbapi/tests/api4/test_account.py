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


def test_favorite_movies():
    tmdbapi.api4.account.favorite_movies(language=LANGUAGE)


def test_favorite_tv_shows():
    tmdbapi.api4.account.favorite_tv_shows(language=LANGUAGE)


def test_lists():
    tmdbapi.api4.account.lists()


def test_rated_movies():
    tmdbapi.api4.account.rated_movies(language=LANGUAGE)


def test_rated_tv_shows():
    tmdbapi.api4.account.rated_tv_shows(language=LANGUAGE)


def test_recommended_movies():
    tmdbapi.api4.account.recommended_movies(language=LANGUAGE)


def test_recommended_tv_shows():
    tmdbapi.api4.account.recommended_tv_shows(language=LANGUAGE)


def test_watchlist_movies():
    tmdbapi.api4.account.watchlist_movies(language=LANGUAGE)


def test_watchlist_tv_shows():
    tmdbapi.api4.account.watchlist_tv_shows(language=LANGUAGE)


def test_watchlist_tv_shows2():
    tmdbapi.api4.account.watchlist_tv_shows()
