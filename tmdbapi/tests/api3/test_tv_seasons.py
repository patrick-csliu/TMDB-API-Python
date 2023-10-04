import sys

import pytest
from ..conftest import DataSharing

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
SEASON_NUM = 2
LANGUAGE = "en_US"


def test_account_states():
    tmdbapi.api3.tv_seasons.account_states(SERIES_ID, SEASON_NUM)


def test_aggregate_credits():
    tmdbapi.api3.tv_seasons.aggregate_credits(SERIES_ID, SEASON_NUM, language=LANGUAGE)


@pytest.mark.dependency(name="details", scope="module")
def test_details():
    json = tmdbapi.api3.tv_seasons.details(SERIES_ID, SEASON_NUM, language=LANGUAGE)
    DataSharing.id = json["id"]


@pytest.mark.dependency(depends=["details"], scope="module")
def test_changes():
    season_id = DataSharing.id
    tmdbapi.api3.tv_seasons.changes(season_id, "2016-05-01", "2016-05-12")


def test_credits():
    tmdbapi.api3.tv_seasons.credits(SERIES_ID, SEASON_NUM, language=LANGUAGE)


def test_external_ids():
    tmdbapi.api3.tv_seasons.external_ids(SERIES_ID, SEASON_NUM)


def test_images():
    tmdbapi.api3.tv_seasons.images(SERIES_ID, SEASON_NUM, language=LANGUAGE)


def test_translations():
    tmdbapi.api3.tv_seasons.translations(SERIES_ID, SEASON_NUM)


def test_videos():
    tmdbapi.api3.tv_seasons.videos(SERIES_ID, SEASON_NUM, language=LANGUAGE)


def test_watch_providers():
    tmdbapi.api3.tv_seasons.watch_providers(SERIES_ID, SEASON_NUM, language=LANGUAGE)
