"""API v3 changes category

"""

from tmdbapi._core import Tmdb
from tmdbapi.exceptions import type_checking

_CHANGES_V3 = {
    "changes-movie-list": {
        "method": "get",
        "params": [
            {"in": "query", "name": "end_date"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "start_date"},
        ],
        "url": "/movie/changes",
    },
    "changes-people-list": {
        "method": "get",
        "params": [
            {"in": "query", "name": "end_date"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "start_date"},
        ],
        "url": "/person/changes",
    },
    "changes-tv-list": {
        "method": "get",
        "params": [
            {"in": "query", "name": "end_date"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "start_date"},
        ],
        "url": "/tv/changes",
    },
}


class _Changes(Tmdb):
    def __init__(self, info_var):
        super().__init__()
        self.category_path = ""
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url=url,
        )

    def change_list(self, use_name, start_date="", end_date="", page=1) -> dict:
        """Wrap the same process for get th change list"""
        self.reset()
        self.use(use_name)
        if start_date != "":
            type_checking("date", start_date)
            self.load_query(start_date=start_date)
        if end_date != "":
            type_checking("date", end_date)
            self.load_query(end_date=end_date)
        self.load_query(page=page)
        return self.request()


def movie_list(start_date="", end_date="", page=1) -> dict:
    """Get a list of all of the movie ids that have been
    changed in the past 24 hours.

    `start_date` and `start_date` is lte and gte
    Format: YYYY-MM-DD
    """
    changes = _Changes(_CHANGES_V3)
    return changes.change_list(
        "changes-movie-list", start_date=start_date, end_date=end_date, page=page
    )


def tv_list(start_date="", end_date="", page=1) -> dict:
    """

    `start_date` and `start_date` is lte and gte
    Format: YYYY-MM-DD
    """
    changes = _Changes(_CHANGES_V3)
    return changes.change_list(
        "changes-tv-list", start_date=start_date, end_date=end_date, page=page
    )


def person_list(start_date="", end_date="", page=1) -> dict:
    """

    `start_date` and `start_date` is lte and gte
    Format: YYYY-MM-DD
    """
    changes = _Changes(_CHANGES_V3)
    return changes.change_list(
        "changes-people-list", start_date=start_date, end_date=end_date, page=page
    )
