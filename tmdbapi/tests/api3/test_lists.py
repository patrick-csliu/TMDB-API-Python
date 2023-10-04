import sys

import pytest

import tmdbapi
from ..conftest import DataSharing


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


MOVIES = [346698, 603692, 109445]


@pytest.mark.dependency(name="lists_a", scope="module")
def test_create():
    json = tmdbapi.api3.lists.create(
        "Test List", description="A description", language="zh"
    )
    DataSharing.id = json["list_id"]


@pytest.mark.dependency(name="lists_b", depends=["lists_a"], scope="module")
def test_add_movie():
    list_id = DataSharing.id
    DataSharing.movie_id = MOVIES[0]
    tmdbapi.api3.lists.add_movie(list_id, MOVIES[0])


@pytest.mark.dependency(name="lists_c", depends=["lists_b"], scope="module")
def test_check_item_status():
    list_id = DataSharing.id
    tmdbapi.api3.lists.check_item_status(list_id, MOVIES[0], "en-US")


@pytest.mark.dependency(name="lists_d", depends=["lists_c"], scope="module")
def test_clear():
    list_id = DataSharing.id
    tmdbapi.api3.lists.clear(list_id)
    # add movie back
    tmdbapi.api3.lists.add_movie(list_id, MOVIES[1])
    tmdbapi.api3.lists.add_movie(list_id, MOVIES[2])


@pytest.mark.dependency(name="lists_e", depends=["lists_d"], scope="module")
def test_details():
    list_id = DataSharing.id
    tmdbapi.api3.lists.details(list_id)


@pytest.mark.dependency(name="lists_f", depends=["lists_e"], scope="module")
def test_remove_movie():
    list_id = DataSharing.id
    tmdbapi.api3.lists.remove_movie(list_id, MOVIES[1])


@pytest.mark.dependency(name="lists_g", depends=["lists_f"], scope="module")
def test_delete():
    list_id = DataSharing.id
    tmdbapi.api3.lists.delete(list_id)
