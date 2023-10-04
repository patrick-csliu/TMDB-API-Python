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
        self.category_path = "/list"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url=url,
        )


def add_movie(list_id: int, movie_id: int) -> dict:
    """Add a movie to a list."""
    lists = _Lists(_LISTS_V3)
    lists.reset()
    lists.use("list-add-movie")
    lists.load_path_arg(list_id=list_id)
    lists.load_query(lists.check_token())
    lists.load_json({"media_id": movie_id})
    return lists.request()


def check_item_status(list_id: int, movie_id: int, language: str = None) -> dict:
    """Use this method to check if an item has already been added
    to the list.
    """
    lists = _Lists(_LISTS_V3)
    lists.reset()
    lists.use("list-check-item-status")
    lists.load_path_arg(list_id=list_id)
    lists.language(language)
    lists.load_query(movie_id=movie_id)
    return lists.request()


def clear(list_id: int) -> dict:
    """Clear all items from a list."""
    lists = _Lists(_LISTS_V3)
    lists.reset()
    lists.use("list-clear")
    lists.load_path_arg(list_id=list_id)
    lists.load_query(lists.check_token())
    lists.load_query(confirm=True)
    return lists.request()


def create(name: str, description: str, language="en") -> dict:
    lists = _Lists(_LISTS_V3)
    lists.reset()
    lists.use("list-create")
    lists.load_query(lists.check_token())
    lists.load_json({"name": name, "description": description, "language": language})
    return lists.request()


def delete(list_id: int) -> dict:
    """Delete a list."""
    lists = _Lists(_LISTS_V3)
    lists.reset()
    lists.use("list-delete")
    lists.load_path_arg(list_id=list_id)
    lists.load_query(lists.check_token())
    return lists.request()


def details(list_id: int, language: str = None) -> dict:
    lists = _Lists(_LISTS_V3)
    lists.reset()
    lists.use("list-details")
    lists.load_path_arg(list_id=list_id)
    lists.language(language)
    return lists.request()


def remove_movie(list_id: int, movie_id: int) -> dict:
    """Remove a movie from a list."""
    lists = _Lists(_LISTS_V3)
    lists.reset()
    lists.use("list-remove-movie")
    lists.load_path_arg(list_id=list_id)
    lists.load_query(lists.check_token())
    lists.load_json({"media_id": movie_id})
    return lists.request()
