"""API v3 people category

"""

from tmdbapi._core import Tmdb
from tmdbapi.exceptions import type_checking


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
        self.base_path = "/person"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url = url,
        )

_people = _People(_PEOPLE_V3)


def popular(page=1, language: str = None) -> dict:
    """Get a list of people ordered by popularity.
    """
    _people.reset()
    _people.use("person-popular-list")
    _people.language(language)
    _people.load_query(page=page)
    return _people.request()


def details(person_id: int, append_to_response="videos,images",
            language: str = None) -> dict:
    """Query the top level details of a person.
    """
    _people.reset()
    _people.use("person-details")
    _people.load_path_arg(person_id=person_id)
    _people.language(language)
    _people.load_query(append_to_response=append_to_response)
    return _people.request()


def changes(person_id: int, start_date="", end_date="",
            page=1) -> dict:
    """Get the recent changes for a person.
    
    `start_date` and `start_date` is lte and gte
    Format: YYYY-MM-DD
    """
    type_checking("date", start_date)
    type_checking("date", end_date)
    _people.reset()
    _people.use("person-changes")
    _people.load_path_arg(person_id=person_id)
    if start_date != "":
        _people.load_query(start_date=start_date)
    if end_date != "":
        _people.load_query(end_date=end_date)
    _people.load_query(page=page)
    return _people.request()


def combined_credits(person_id: int, language: str = None) -> dict:
    """Get the combined movie and TV credits that belong to a person.
    """
    _people.reset()
    _people.use("person-combined-credits")
    _people.load_path_arg(person_id=person_id)
    _people.language(language)
    return _people.request()


def external_ids(person_id: int) -> dict:
    """Get the external ID's that belong to a person.
    """
    _people.reset()
    _people.use("person-external-ids")
    _people.load_path_arg(person_id=person_id)
    return _people.request()


def images(person_id: int) -> dict:
    """Get the profile images that belong to a person.
    """
    _people.reset()
    _people.use("person-images")
    _people.load_path_arg(person_id=person_id)
    return _people.request()


def latest() -> dict:
    """Get the newest created person. This is a live response and 
    will continuously change.
    """
    _people.reset()
    _people.use("person-latest-id")
    return _people.request()


def movie_credits(person_id: int, language: str = None) -> dict:
    """Get the movie credits for a person.
    """
    _people.reset()
    _people.use("person-movie-credits")
    _people.load_path_arg(person_id=person_id)
    _people.language(language)
    return _people.request()


def tv_credits(person_id: int, language: str = None) -> dict:
    """Get the TV credits that belong to a person.
    """
    _people.reset()
    _people.use("person-tv-credits")
    _people.load_path_arg(person_id=person_id)
    _people.language(language)
    return _people.request()


def tagged_images(person_id: int, page=1) -> dict:
    """Get the tagged images for a person.
    """
    _people.reset()
    _people.use("person-tagged-images")
    _people.load_path_arg(person_id=person_id)
    _people.load_query(page=page)
    return _people.request()


def translations(person_id: int) -> dict:
    """Get the translations that belong to a person.
    """
    _people.reset()
    _people.use("translations")
    _people.load_path_arg(person_id=person_id)
    return _people.request()
