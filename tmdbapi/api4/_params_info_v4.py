_ACCOUNT = {
    "account-favorite-movies": {
        "description": "Get a user's list of favourite " "movies.",
        "method": "get",
        "params": [
            {"in": "path", "name": "account_object_id"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "language"},
        ],
        "url": "/4/account/{account_object_id}/movie/favorites",
    },
    "account-favorite-tv": {
        "description": "Get a user's list of favourite TV " "shows.",
        "method": "get",
        "params": [
            {"in": "path", "name": "account_object_id"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "language"},
        ],
        "url": "/4/account/{account_object_id}/tv/favorites",
    },
    "account-lists": {
        "description": "Get all of the lists you've created.",
        "method": "get",
        "params": [
            {"in": "path", "name": "account_object_id"},
            {"in": "query", "name": "page"},
        ],
        "url": "/4/account/{account_object_id}/lists",
    },
    "account-movie-recommendations": {
        "description": "Get a user's list of " "recommended movies.",
        "method": "get",
        "params": [
            {"in": "path", "name": "account_object_id"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "language"},
        ],
        "url": "/4/account/{account_object_id}/movie/recommendations",
    },
    "account-movie-watchlist": {
        "description": "Get a user's movie watchlist.",
        "method": "get",
        "params": [
            {"in": "path", "name": "account_object_id"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "language"},
        ],
        "url": "/4/account/{account_object_id}/movie/watchlist",
    },
    "account-rated-movies": {
        "description": "Get a user's rated movies.",
        "method": "get",
        "params": [
            {"in": "path", "name": "account_object_id"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "language"},
        ],
        "url": "/4/account/{account_object_id}/movie/rated",
    },
    "account-rated-tv": {
        "description": "Get a user's rated TV shows.",
        "method": "get",
        "params": [
            {"in": "path", "name": "account_object_id"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "language"},
        ],
        "url": "/4/account/{account_object_id}/tv/rated",
    },
    "account-tv-recommendations": {
        "description": "Get a user's list of " "recommended TV shows.",
        "method": "get",
        "params": [
            {"in": "path", "name": "account_object_id"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "language"},
        ],
        "url": "/4/account/{account_object_id}/tv/recommendations",
    },
    "account-tv-watchlist": {
        "description": "Get a user's TV watchlist.",
        "method": "get",
        "params": [
            {"in": "path", "name": "account_object_id"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "language"},
        ],
        "url": "/4/account/{account_object_id}/tv/watchlist",
    },
}
_AUTH = {
    "auth-create-access-token": {
        "description": "",
        "method": "post",
        "params": [{"in": "body", "name": "RAW_BODY"}],
        "url": "/4/auth/access_token",
    },
    "auth-create-request-token": {
        "description": "",
        "method": "post",
        "params": [{"in": "body", "name": "RAW_BODY"}],
        "url": "/4/auth/request_token",
    },
    "auth-logout": {
        "description": "Log out of a session.",
        "method": "delete",
        "params": [{"in": "body", "name": "RAW_BODY"}],
        "url": "/4/auth/access_token",
    },
}
_LISTS = {
    "list-add-items": {
        "description": "Add items to a list.",
        "method": "post",
        "params": [
            {"in": "path", "name": "list_id"},
            {"in": "body", "name": "RAW_BODY"},
        ],
        "url": "/4/{list_id}/items",
    },
    "list-clear": {
        "description": "Clear all of the items on a list.",
        "method": "get",
        "params": [{"in": "path", "name": "list_id"}],
        "url": "/4/list/{list_id}/clear",
    },
    "list-create": {
        "description": "Create a new list.",
        "method": "post",
        "params": [{"in": "body", "name": "RAW_BODY"}],
        "url": "/4/list",
    },
    "list-delete": {
        "description": "Delete a list.",
        "method": "delete",
        "params": [{"in": "path", "name": "list_id"}],
        "url": "/4/{list_id}",
    },
    "list-details": {
        "description": "Retrieve a list by id.",
        "method": "get",
        "params": [{"in": "path", "name": "{list_id}"}],
        "url": "/4/list/{list_id}",
    },
    "list-item-status": {
        "description": "Check if an item is on a list.",
        "method": "get",
        "params": [
            {"in": "path", "name": "list_id"},
            {"in": "query", "name": "media_id"},
            {"in": "query", "name": "media_type"},
        ],
        "url": "/4/list/{list_id}/item_status",
    },
    "list-remove-items": {
        "description": "Remove items from a list",
        "method": "delete",
        "params": [
            {"in": "path", "name": "list_id"},
            {"in": "body", "name": "RAW_BODY"},
        ],
        "url": "/4/list/{list_id}/items",
    },
    "list-update": {
        "description": "Update the details of a list.",
        "method": "put",
        "params": [
            {"in": "path", "name": "list_id"},
            {"in": "body", "name": "RAW_BODY"},
        ],
        "url": "/4/{list_id}",
    },
    "list-update-items": {
        "description": "Update an individual item on a list",
        "method": "put",
        "params": [{"in": "body", "name": "RAW_BODY"}],
        "url": "/4/list/{list_id}/items",
    },
}
