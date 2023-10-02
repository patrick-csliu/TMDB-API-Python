"""API v3 lists category

"""

from tmdbapi._core import Tmdb


_LISTS_V3 = {
    "list-add-movie": {
        "method": "post",
        "params": [
            {"in": "path", "name": "list_id"},
            {"in": "query", "name": "session_id"},
            {"in": "body", "name": "RAW_BODY"},
        ],
        "url": "/{list_id}/add_item",
    },
    "list-check-item-status": {
        "method": "get",
        "params": [
            {"in": "path", "name": "list_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "movie_id"},
        ],
        "url": "/{list_id}/item_status",
    },
    "list-clear": {
        "method": "post",
        "params": [
            {"in": "path", "name": "list_id"},
            {"in": "query", "name": "session_id"},
            {"in": "query", "name": "confirm"},
        ],
        "url": "/{list_id}/clear",
    },
    "list-create": {
        "method": "post",
        "params": [
            {"in": "query", "name": "session_id"},
            {"in": "body", "name": "RAW_BODY"},
        ],
        "url": "",
    },
    "list-delete": {
        "method": "delete",
        "params": [
            {"in": "path", "name": "list_id"},
            {"in": "query", "name": "session_id"},
        ],
        "url": "/{list_id}",
    },
    "list-details": {
        "method": "get",
        "params": [
            {"in": "path", "name": "list_id"},
            {"in": "query", "name": "language"},
        ],
        "url": "/{list_id}",
    },
    "list-remove-movie": {
        "method": "post",
        "params": [
            {"in": "path", "name": "list_id"},
            {"in": "query", "name": "session_id"},
            {"in": "body", "name": "RAW_BODY"},
        ],
        "url": "/{list_id}/remove_item",
    },
}


class _Lists(Tmdb):

    def __init__(self, info_var):
        super().__init__()
        self.base_path = "/list"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url = url,
        )

_lists = _Lists(_LISTS_V3)


def add_movie(list_id: int, movie_id: int) -> dict:
    """Add a movie to a list.
    """
    _lists.reset()
    _lists.use("list-add-movie")
    _lists.load_path_arg(list_id=list_id)
    _lists.load_query(_lists.check_token())
    _lists.load_json({"media_id": movie_id})
    return _lists.request()


def check_item_status(list_id: int, movie_id: int,
                      language: str = None) -> dict:
    """Use this method to check if an item has already been added 
    to the list.
    """
    _lists.reset()
    _lists.use("list-check-item-status")
    _lists.load_path_arg(list_id=list_id)
    _lists.language(language)
    _lists.load_query(movie_id=movie_id)
    return _lists.request()


def clear(list_id: int) -> dict:
    """Clear all items from a list.
    """
    _lists.reset()
    _lists.use("list-clear")
    _lists.load_path_arg(list_id=list_id)
    _lists.load_query(_lists.check_token())
    _lists.load_query(confirm="true")
    return _lists.request()


def create(name: str, description: str, language='en') -> dict:

    _lists.reset()
    _lists.use("list-create")
    _lists.load_query(_lists.check_token())
    _lists.load_json(
        {
            "name": name,
            "description": description,
            "language": language
        }
    )
    return _lists.request()


def delete(list_id: int) -> dict:
    """Delete a list.
    """
    _lists.reset()
    _lists.use("list-delete")
    _lists.load_path_arg(list_id=list_id)
    _lists.load_query(_lists.check_token())
    return _lists.request()


def details(list_id: int, language: str = None) -> dict:

    _lists.reset()
    _lists.use("list-details")
    _lists.load_path_arg(list_id=list_id)
    _lists.language(language)
    return _lists.request()


def remove_movie(list_id: int, movie_id: int) -> dict:
    """Remove a movie from a list.
    """
    _lists.reset()
    _lists.use("list-remove-movie")
    _lists.load_path_arg(list_id=list_id)
    _lists.load_query(_lists.check_token())
    _lists.load_json({"media_id": movie_id})
    return _lists.request()
