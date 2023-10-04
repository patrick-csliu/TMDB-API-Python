"""API v3 people category

"""

from tmdbapi._core import Tmdb
from tmdbapi.exceptions import ServiceDeprecationWarning, type_checking

_PEOPLE_V3 = {
    "person-popular-list": {
        "method": "get",
        "params": [
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
        ],
        "url": "/popular",
    },
    "person-changes": {
        "method": "get",
        "params": [
            {"in": "path", "name": "person_id"},
            {"in": "query", "name": "end_date"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "start_date"},
        ],
        "url": "/{person_id}/changes",
    },
    "person-combined-credits": {
        "method": "get",
        "params": [
            {"in": "path", "name": "person_id"},
            {"in": "query", "name": "language"},
        ],
        "url": "/{person_id}/combined_credits",
    },
    "person-details": {
        "method": "get",
        "params": [
            {"in": "path", "name": "person_id"},
            {"in": "query", "name": "append_to_response"},
            {"in": "query", "name": "language"},
        ],
        "url": "/{person_id}",
    },
    "person-external-ids": {
        "method": "get",
        "params": [{"in": "path", "name": "person_id"}],
        "url": "/{person_id}/external_ids",
    },
    "person-images": {
        "method": "get",
        "params": [{"in": "path", "name": "person_id"}],
        "url": "/{person_id}/images",
    },
    "person-latest-id": {"method": "get", "params": [], "url": "/latest"},
    "person-movie-credits": {
        "method": "get",
        "params": [
            {"in": "path", "name": "person_id"},
            {"in": "query", "name": "language"},
        ],
        "url": "/{person_id}/movie_credits",
    },
    "person-tagged-images": {
        "method": "get",
        "params": [
            {"in": "path", "name": "person_id"},
            {"in": "query", "name": "page"},
        ],
        "url": "/{person_id}/tagged_images",
    },
    "person-tv-credits": {
        "method": "get",
        "params": [
            {"in": "path", "name": "person_id"},
            {"in": "query", "name": "language"},
        ],
        "url": "/{person_id}/tv_credits",
    },
    "translations": {
        "method": "get",
        "params": [{"in": "path", "name": "person_id"}],
        "url": "/{person_id}/translations",
    },
}


class _People(Tmdb):
    def __init__(self, info_var):
        super().__init__()
        self.category_path = "/person"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url=url,
        )


def popular(page=1, language: str = None) -> dict:
    """Get a list of people ordered by popularity."""
    people = _People(_PEOPLE_V3)
    people.reset()
    people.use("person-popular-list")
    people.language(language)
    people.load_query(page=page)
    return people.request()


def details(
    person_id: int, append_to_response="videos,images", language: str = None
) -> dict:
    """Query the top level details of a person."""
    people = _People(_PEOPLE_V3)
    people.reset()
    people.use("person-details")
    people.load_path_arg(person_id=person_id)
    people.language(language)
    people.load_query(append_to_response=append_to_response)
    return people.request()


def changes(person_id: int, start_date="", end_date="", page=1) -> dict:
    """Get the recent changes for a person.

    `start_date` and `start_date` is lte and gte
    Format: YYYY-MM-DD
    """
    people = _People(_PEOPLE_V3)
    people.reset()
    people.use("person-changes")
    people.load_path_arg(person_id=person_id)
    if start_date != "":
        type_checking("date", start_date)
        people.load_query(start_date=start_date)
    if end_date != "":
        type_checking("date", end_date)
        people.load_query(end_date=end_date)
    people.load_query(page=page)
    return people.request()


def combined_credits(person_id: int, language: str = None) -> dict:
    """Get the combined movie and TV credits that belong to a person."""
    people = _People(_PEOPLE_V3)
    people.reset()
    people.use("person-combined-credits")
    people.load_path_arg(person_id=person_id)
    people.language(language)
    return people.request()


def external_ids(person_id: int) -> dict:
    """Get the external ID's that belong to a person."""
    people = _People(_PEOPLE_V3)
    people.reset()
    people.use("person-external-ids")
    people.load_path_arg(person_id=person_id)
    return people.request()


def images(person_id: int) -> dict:
    """Get the profile images that belong to a person."""
    people = _People(_PEOPLE_V3)
    people.reset()
    people.use("person-images")
    people.load_path_arg(person_id=person_id)
    return people.request()


def latest() -> dict:
    """Get the newest created person. This is a live response and
    will continuously change.
    """
    people = _People(_PEOPLE_V3)
    people.reset()
    people.use("person-latest-id")
    return people.request()


def movie_credits(person_id: int, language: str = None) -> dict:
    """Get the movie credits for a person."""
    people = _People(_PEOPLE_V3)
    people.reset()
    people.use("person-movie-credits")
    people.load_path_arg(person_id=person_id)
    people.language(language)
    return people.request()


def tv_credits(person_id: int, language: str = None) -> dict:
    """Get the TV credits that belong to a person."""
    people = _People(_PEOPLE_V3)
    people.reset()
    people.use("person-tv-credits")
    people.load_path_arg(person_id=person_id)
    people.language(language)
    return people.request()


def tagged_images(person_id: int, page=1) -> dict:
    """Get the tagged images for a person."""
    people = _People(_PEOPLE_V3)
    ServiceDeprecationWarning("people.tagged_images method is deprecated.")
    people.reset()
    people.use("person-tagged-images")
    people.load_path_arg(person_id=person_id)
    people.load_query(page=page)
    return people.request()


def translations(person_id: int) -> dict:
    """Get the translations that belong to a person."""
    people = _People(_PEOPLE_V3)
    people.reset()
    people.use("translations")
    people.load_path_arg(person_id=person_id)
    return people.request()
