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


MOVIE_ID = 372058


def test_account_states():
    tmdbapi.api3.movies.account_states(MOVIE_ID)


# def test_account_states_guest_session():
#     tmdbapi.api3.movies.account_states()


def test_alternative_titles():
    tmdbapi.api3.movies.alternative_titles(MOVIE_ID, "TW")


def test_changes():
    tmdbapi.api3.movies.changes(MOVIE_ID, "2017-01-01", "2017-01-15")


def test_credits():
    tmdbapi.api3.movies.credits(MOVIE_ID, "en-US")


@pytest.mark.dependency(name="add_rate", scope="module")
def test_add_rating():
    tmdbapi.api3.movies.add_rating(MOVIE_ID, 6)


@pytest.mark.dependency(depends=["add_rate"], scope="module")
def test_delete_rating():
    tmdbapi.api3.movies.delete_rating(MOVIE_ID)


def test_details():
    tmdbapi.api3.movies.details(MOVIE_ID, language="zh-TW")


def test_external_ids():
    tmdbapi.api3.movies.external_ids(MOVIE_ID)


def test_images():
    tmdbapi.api3.movies.images(MOVIE_ID, include_image_language="zh")


def test_keywords():
    tmdbapi.api3.movies.keywords(MOVIE_ID)


def test_latest():
    tmdbapi.api3.movies.latest()


def test_lists():
    tmdbapi.api3.movies.lists(MOVIE_ID)


def test_recommendations():
    tmdbapi.api3.movies.recommendations(MOVIE_ID, language="zh-TW")


def test_release_dates():
    tmdbapi.api3.movies.release_dates(MOVIE_ID)


def test_reviews():
    tmdbapi.api3.movies.reviews(MOVIE_ID, language="zh-TW")


def test_similar():
    tmdbapi.api3.movies.similar(MOVIE_ID, language="zh-TW")


def test_translations():
    tmdbapi.api3.movies.translations(MOVIE_ID)


def test_videos():
    tmdbapi.api3.movies.videos(MOVIE_ID, language="zh-TW")


def test_watch_providers():
    tmdbapi.api3.movies.watch_providers(MOVIE_ID)
