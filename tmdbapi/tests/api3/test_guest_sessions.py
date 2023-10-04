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


LANGUAGE = "en-US"


@pytest.mark.dependency(name="guest_session", scope="module")
def test_create_guest_session():
    json = tmdbapi.api3.authentication.create_guest_session()
    DataSharing.id = json["guest_session_id"]


@pytest.mark.dependency(depends=["guest_session"], scope="module")
def test_rated_movies():
    gid = DataSharing.id
    tmdbapi.api3.guest_sessions.rated_movies(gid, LANGUAGE, asc_sort=False)


@pytest.mark.dependency(depends=["guest_session"], scope="module")
def test_rated_tv():
    gid = DataSharing.id
    tmdbapi.api3.guest_sessions.rated_tv(gid, LANGUAGE, asc_sort=False)


@pytest.mark.dependency(depends=["guest_session"], scope="module")
def test_rated_tv_episodes():
    gid = DataSharing.id
    tmdbapi.api3.guest_sessions.rated_tv_episodes(gid, LANGUAGE, asc_sort=False)
