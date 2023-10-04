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
EPISODE_NUM = 1
LANGUAGE = "en_US"


def test_account_states():
    tmdbapi.api3.tv_episodes.account_states(SERIES_ID, SEASON_NUM, EPISODE_NUM)


@pytest.mark.dependency(name="add_rate", scope="module")
def test_add_rating():
    tmdbapi.api3.tv_episodes.add_rating(SERIES_ID, SEASON_NUM, EPISODE_NUM, 3)


@pytest.mark.dependency(depends=["add_rate"], scope="module")
def test_delete_rating():
    tmdbapi.api3.tv_episodes.delete_rating(SERIES_ID, SEASON_NUM, EPISODE_NUM)


@pytest.mark.dependency(name="details", scope="module")
def test_details():
    tmdbapi.api3.tv_episodes.details(
        SERIES_ID, SEASON_NUM, EPISODE_NUM, language=LANGUAGE
    )


@pytest.mark.dependency(depends=["details"], scope="module")
def test_changes():
    episode_id = DataSharing.id
    tmdbapi.api3.tv_episodes.changes(episode_id)


def test_credits():
    json = tmdbapi.api3.tv_episodes.credits(
        SERIES_ID, SEASON_NUM, EPISODE_NUM, language=LANGUAGE
    )
    DataSharing.id = json["id"]


def test_external_ids():
    tmdbapi.api3.tv_episodes.external_ids(SERIES_ID, SEASON_NUM, EPISODE_NUM)


def test_images():
    tmdbapi.api3.tv_episodes.images(
        SERIES_ID, SEASON_NUM, EPISODE_NUM, include_image_language="en"
    )


def test_translations():
    tmdbapi.api3.tv_episodes.translations(SERIES_ID, SEASON_NUM, EPISODE_NUM)


def test_videos():
    tmdbapi.api3.tv_episodes.videos(SERIES_ID, SEASON_NUM, EPISODE_NUM, "eb-US", "en")
