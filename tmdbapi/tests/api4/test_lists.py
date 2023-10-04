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


ITEMS1 = [
    {"media_type": "movie", "media_id": 346698, "comment": "Amazing!"},
    {"media_type": "tv", "media_id": 71712, "comment": "Good"},
    {"media_type": "movie", "media_id": 603692, "comment": "Not good"},
]
ITEMS2 = [["tv", 1416, "A"], ["movie", 109445, "B"], ["tv", 4614, "C"]]


@pytest.mark.dependency(name="lists_a", scope="module")
def test_create():
    json = tmdbapi.api4.lists.create(
        "Test List",
        "This is a list for test (v4)",
        False,
        "primary_release_date.asc",
        "zh-TW",
        "TW",
    )
    DataSharing.id = json["id"]


@pytest.mark.dependency(name="lists_b", depends=["lists_a"], scope="module")
def test_add_items():
    list_id = DataSharing.id
    tmdbapi.api4.lists.add_items(list_id, ITEMS1)


@pytest.mark.dependency(name="lists_c", depends=["lists_b"], scope="module")
def test_item_status():
    list_id = DataSharing.id
    tmdbapi.api4.lists.item_status(
        list_id, ITEMS1[1]["media_id"], ITEMS1[1]["media_type"]
    )


@pytest.mark.dependency(name="lists_d", depends=["lists_c"], scope="module")
def test_details():
    list_id = DataSharing.id
    tmdbapi.api4.lists.details(list_id)


@pytest.mark.dependency(name="lists_e", depends=["lists_d"], scope="module")
def test_remove_items():
    list_id = DataSharing.id
    tmdbapi.api4.lists.remove_items(list_id, ITEMS1[:2])


@pytest.mark.dependency(name="lists_f", depends=["lists_e"], scope="module")
def test_update():
    list_id = DataSharing.id
    tmdbapi.api4.lists.update(
        list_id,
        "Test List 2",
        "This is a list for test (v4)2",
        False,
        "title.desc",
        "en-US",
        "U",
    )


@pytest.mark.dependency(name="lists_g", depends=["lists_f"], scope="module")
def test_update_items():
    list_id = DataSharing.id
    tmdbapi.api4.lists.update_items(list_id, ITEMS2)


@pytest.mark.dependency(name="lists_h", depends=["lists_g"], scope="module")
def test_clear():
    list_id = DataSharing.id
    tmdbapi.api4.lists.clear(list_id)


@pytest.mark.dependency(name="lists_i", depends=["lists_a"], scope="module")
def test_delete():
    list_id = DataSharing.id
    tmdbapi.api4.lists.delete(list_id)
