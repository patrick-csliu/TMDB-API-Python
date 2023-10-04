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


SERIES_ID = 1416
LANGUAGE = "en_US"


def test_account_states():
    tmdbapi.api3.tv_series.account_states(SERIES_ID)


@pytest.mark.dependency(name="add_rate", scope="module")
def test_add_rating():
    tmdbapi.api3.tv_series.add_rating(SERIES_ID, 3)


@pytest.mark.dependency(depends=["add_rate"], scope="module")
def test_delete_rating():
    tmdbapi.api3.tv_series.delete_rating(SERIES_ID)


def test_aggregate_credits():
    tmdbapi.api3.tv_series.aggregate_credits(SERIES_ID, LANGUAGE)


def test_alternative_titles():
    tmdbapi.api3.tv_series.alternative_titles(SERIES_ID)


def test_changes():
    tmdbapi.api3.tv_series.changes(SERIES_ID, "2017-01-01", "2017-01-12")


def test_content_ratings():
    tmdbapi.api3.tv_series.content_ratings(SERIES_ID)


def test_credits():
    tmdbapi.api3.tv_series.credits(SERIES_ID, LANGUAGE)


def test_details():
    tmdbapi.api3.tv_series.details(SERIES_ID, language=LANGUAGE)


def test_episode_groups():
    tmdbapi.api3.tv_series.episode_groups(SERIES_ID)


def test_external_ids():
    tmdbapi.api3.tv_series.external_ids(SERIES_ID)


def test_images():
    tmdbapi.api3.tv_series.images(SERIES_ID, include_image_language="zh")


def test_keywords():
    tmdbapi.api3.tv_series.keywords(SERIES_ID)


def test_latest():
    tmdbapi.api3.tv_series.latest()


def test_recommendations():
    tmdbapi.api3.tv_series.recommendations(SERIES_ID, language=LANGUAGE)


def test_reviews():
    tmdbapi.api3.tv_series.reviews(SERIES_ID, language=LANGUAGE)


def test_screened_theatrically():
    tmdbapi.api3.tv_series.screened_theatrically(SERIES_ID)


def test_similar():
    tmdbapi.api3.tv_series.similar(SERIES_ID, language=LANGUAGE)


def test_translations():
    tmdbapi.api3.tv_series.translations(SERIES_ID)


def test_videos():
    tmdbapi.api3.tv_series.videos(SERIES_ID)


def test_watch_providers():
    tmdbapi.api3.tv_series.watch_providers(SERIES_ID)
