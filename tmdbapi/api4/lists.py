"""API v4 lists category

"""

import tmdbapi
from tmdbapi._core import Tmdb
from tmdbapi.exceptions import type_checking

_LISTS_V4 = {
    "list-add-items": {
        "method": "post",
        "params": [
            {"in": "path", "name": "list_id"},
            {"in": "body", "name": "RAW_BODY"},
        ],
        "url": "/{list_id}/items",
    },
    "list-clear": {
        "method": "get",
        "params": [{"in": "path", "name": "list_id"}],
        "url": "/{list_id}/clear",
    },
    "list-create": {
        "method": "post",
        "params": [{"in": "body", "name": "RAW_BODY"}],
        "url": "",
    },
    "list-delete": {
        "method": "delete",
        "params": [{"in": "path", "name": "list_id"}],
        "url": "/{list_id}",
    },
    "list-details": {
        "method": "get",
        "params": [{"in": "path", "name": "{list_id}"}],
        "url": "/{list_id}",
    },
    "list-item-status": {
        "method": "get",
        "params": [
            {"in": "path", "name": "list_id"},
            {"in": "query", "name": "media_id"},
            {"in": "query", "name": "media_type"},
        ],
        "url": "/{list_id}/item_status",
    },
    "list-remove-items": {
        "method": "delete",
        "params": [
            {"in": "path", "name": "list_id"},
            {"in": "body", "name": "RAW_BODY"},
        ],
        "url": "/{list_id}/items",
    },
    "list-update": {
        "method": "put",
        "params": [
            {"in": "path", "name": "list_id"},
            {"in": "body", "name": "RAW_BODY"},
        ],
        "url": "/{list_id}",
    },
    "list-update-items": {
        "method": "put",
        "params": [{"in": "body", "name": "RAW_BODY"}],
        "url": "/{list_id}/items",
    },
}


class _Lists(Tmdb):
    def __init__(self, info_var):
        super().__init__()
        self.category_path = "/list"
        self.info_var = info_var

    def request(self) -> dict:
        tmdbapi.setting.set(use_access_token=True)
        url = self.build_url(4)
        return self.request_raw(
            url=url,
        )


def details(list_id: int) -> dict:
    """Retrieve a list by id."""
    lists = _Lists(_LISTS_V4)
    lists.reset()
    lists.use("list-details")
    lists.load_path_arg(list_id=list_id)
    return lists.request()


def add_items(list_id: int, items: list) -> dict:
    """Add items to a list.

    Parameters
    ----------
    list_id : int
        The ID of the list.
    items : list
        A list of items to add. It supports three types of list items:
        Some items may not have comments. For tuples and lists, their length
        can be 2, while for dictionaries, the 'comment' key may be absent.

        .. code-block:: python

            # 1.
            [
                ("movie", 194662, "Amazing movie!"),
                ("movie", 76203, "Wow."),
            ]

            # 2.
            [
                ["movie", 194662, "Amazing movie!"],
                ["movie", 76203, "Wow."],
            ]

            # 3.
            [
                {
                    "media_type": "movie",
                    "media_id": 194662,
                    "comment": "Amazing movie!"
                },
                {
                    "media_type": "movie",
                    "media_id": 76203,
                    "comment": "Wow."
                },
            ]

    Returns
    -------
    dict
        The response from the API.
    """
    lists = _Lists(_LISTS_V4)
    lists.reset()
    lists.use("list-add-items")
    lists.load_path_arg(list_id=list_id)
    lists.load_json(_pack_items(items))
    return lists.request()


def clear(list_id: int) -> dict:
    """Clear all of the items on a list."""
    lists = _Lists(_LISTS_V4)
    lists.reset()
    lists.use("list-clear")
    lists.load_path_arg(list_id=list_id)
    return lists.request()


def create(
    name: str,
    description="",
    public=False,
    sort_by="original_order.asc",
    language: str = None,
    country: str = None,
) -> dict:
    """Create a new list.

    Parameters
    ----------
    name : str
        The name of the list.
    description : str, optional
        The description of the list, by default ""
    public : bool, optional
        By default False
    sort_by : str, optional
        valid values:
        ```
        original_order.asc
        original_order.desc
        vote_average.asc
        vote_average.desc
        primary_release_date.asc
        primary_release_date.desc
        title.asc
        title.desc
        ```
        , by default "original_order.asc"
    language : str, optional
        iso_639_1 format, by default None
    country : str, optional
        iso_3166_1 format, by default None

    Returns
    -------
    dict
        return from api
    """
    lists = _Lists(_LISTS_V4)
    type_checking("list_sort_by", sort_by)
    lists.reset()
    lists.use("list-create")
    payload = {
        "description": description,
        "name": name,
        "iso_3166_1": "US",
        "iso_639_1": "en",
        "public": public,
        "sort_by": sort_by,
    }
    if language is not None:
        payload["iso_639_1"] = language
    if country is not None:
        payload["iso_3166_1"] = country
    lists.load_json(payload)
    return lists.request()


def delete(list_id: int) -> dict:
    """Delete a list."""
    lists = _Lists(_LISTS_V4)
    lists.reset()
    lists.use("list-delete")
    lists.load_path_arg(list_id=list_id)
    return lists.request()


def item_status(list_id: int, media_id: int, media_type: str) -> dict:
    """Check if an item is on a list."""
    lists = _Lists(_LISTS_V4)
    type_checking("media_type", media_type)
    lists.reset()
    lists.use("list-item-status")
    lists.load_path_arg(list_id=list_id)
    lists.load_query(media_id=media_id, media_type=media_type)
    return lists.request()


def remove_items(list_id: int, items: list) -> dict:
    """Remove items from a list.

    Parameters
    ----------
    list_id : int
        The list id.
    items : list
        Support three types of list.

        .. code-block:: python

            # 1.
            [
                ("movie", 194662),
                ("movie", 76203),
            ]

            # 2.
            [
                ["movie", 194662],
                ["movie", 76203],
            ]

            # 3.
            [
                {
                    "media_type": "movie",
                    "media_id": 194662,
                },
                {
                    "media_type": "movie",
                    "media_id": 76203,
                },
            ]

    Returns
    -------
    dict
        return from api
    """
    lists = _Lists(_LISTS_V4)
    lists.reset()
    lists.use("list-remove-items")
    lists.load_path_arg(list_id=list_id)
    lists.load_json(_pack_items(items))
    return lists.request()


def update(
    list_id: int,
    name: str = None,
    description: str = None,
    public: bool = None,
    sort_by: str = None,
    language: str = None,
    country: str = None,
) -> dict:
    """Update the details of a list.

    Parameters
    ----------
    list_id : int
        The list id.
    name : str, optional
        The name of the list., by default None
    description : str, optional
        The description of the list, by default None
    public : bool, optional
        By default None
    sort_by : str, optional
        valid values:
        ```
        original_order.asc
        original_order.desc
        vote_average.asc
        vote_average.desc
        primary_release_date.asc
        primary_release_date.desc
        title.asc
        title.desc
        ```
        , by default None
    language : str, optional
        iso_639_1 format, by default None
    country : str, optional
        iso_3166_1 format, by default None

    Returns
    -------
    dict
        return from api
    """
    lists = _Lists(_LISTS_V4)
    type_checking("list_sort_by", sort_by)
    lists.reset()
    lists.use("list-update")
    lists.load_path_arg(list_id=list_id)
    payload = {}
    if language is not None:
        payload["iso_639_1"] = language
    if country is not None:
        payload["iso_3166_1"] = country
    if name is not None:
        payload["name"] = name
    if description is not None:
        payload["description"] = description
    if public is not None:
        payload["public"] = public
    if sort_by is not None:
        payload["sort_by"] = sort_by
    lists.load_json(payload)
    return lists.request()


def update_items(list_id: int, items: list) -> dict:
    """Update an individual item on a list

    Parameters
    ----------
    list_id : int
        The list id.
    items : list
        Support three types of list.
        There might be no comments for items; therefore, for tuples
        and lists, the length could be 2, and for dictionaries, the
        'comment' key might not be present.

        .. code-block:: python

            # 1.
            [
                ("movie", 194662, "Amazing movie!"),
                ("movie", 76203, "Wow."),
            ]

            # 2.
            [
                ["movie", 194662, "Amazing movie!"],
                ["movie", 76203, "Wow."],
            ]

            # 3.
            [
                {
                    "media_type": "movie",
                    "media_id": 194662,
                    "comment": "Amazing movie!"
                },
                {
                    "media_type": "movie",
                    "media_id": 76203,
                    "comment": "Wow."
                },
            ]

    Returns
    -------
    dict
        return from api
    """
    lists = _Lists(_LISTS_V4)
    lists.reset()
    lists.use("list-update-items")
    lists.load_path_arg(list_id=list_id)
    lists.load_json(_pack_items(items))
    return lists.request()


def _pack_items(items: list) -> dict:
    """pack items (tv, movie)

    Parameters
    ----------
    items : list
        A list of items to add. It supports three types of list items:
        Some items may not have comments. For tuples and lists, their length
        can be 2, while for dictionaries, the 'comment' key may be absent.

        .. code-block:: python

            # 1.
            [
                ("movie", 194662, "Amazing movie!"),
                ("movie", 76203, "Wow."),
            ]

            # 2.
            [
                ["movie", 194662, "Amazing movie!"],
                ["movie", 76203, "Wow."],
            ]

            # 3.
            [
                {
                    "media_type": "movie",
                    "media_id": 194662,
                    "comment": "Amazing movie!"
                },
                {
                    "media_type": "movie",
                    "media_id": 76203,
                    "comment": "Wow."
                },
            ]

    Returns
    -------
    dict
        example:

        .. code-block:: python

            {
                "items": [
                    {
                        "media_type": "movie",
                        "media_id": 194662,
                        "comment": "Amazing movie!"
                    },
                    {
                        "media_type": "movie",
                        "media_id": 76203,
                        "comment": "Wow."
                    }
                ]
            }

    """

    def _pack_items_list(items: list[list] | list[tuple]) -> dict:
        packed_items = []
        for item in items:
            if len(item) == 2:
                packed_items.append(
                    {
                        "media_type": item[0],
                        "media_id": item[1],
                    }
                )
            elif len(item) == 3:
                packed_items.append(
                    {
                        "media_type": item[0],
                        "media_id": item[1],
                        "comment": item[2],
                    }
                )
            else:
                raise Exception("items error")
        return {"items": packed_items}

    def _pack_items_dict(items: list[dict]) -> dict:
        return {"items": items}

    if items:
        if isinstance(items[0], (list, tuple)):
            return _pack_items_list(items)
        else:
            return _pack_items_dict(items)
    else:
        raise Exception("items is empty")
