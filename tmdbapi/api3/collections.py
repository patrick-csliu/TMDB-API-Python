"""API v3 collections category

"""

from tmdbapi._core import Tmdb


_COLLECTION_V3 = {
    "collection-details": {
        "method": "get",
        "params": [
            {"in": "path", "name": "collection_id"},
            {"in": "query", "name": "language"},
        ],
        "url": "/{collection_id}",
    },
    "collection-images": {
        "method": "get",
        "params": [
            {"in": "path", "name": "collection_id"},
            {"in": "query", "name": "include_image_language"},
            {"in": "query", "name": "language"},
        ],
        "url": "/{collection_id}/images",
    },
    "collection-translations": {
        "method": "get",
        "params": [{"in": "path", "name": "collection_id"}],
        "url": "/{collection_id}/translations",
    },
}


class _Collection(Tmdb):

    def __init__(self, info_var):
        super().__init__()
        self.base_path = "/collection"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url = url,
        )

_collection = _Collection(_COLLECTION_V3)


def details(collection_id: int, language: str = None) -> dict:
    """Get collection (movie series) details by ID.
    """
    _collection.reset()
    _collection.use("collection-details")
    _collection.load_path_arg(collection_id=collection_id)
    _collection.language(language)
    return _collection.request()


def images(collection_id: int, language: str = None,
           include_image_language="") -> dict:
    """Get the images that belong to a collection.
    """
    _collection.reset()
    _collection.use("collection-images")
    _collection.load_path_arg(collection_id=collection_id)
    _collection.language(language)
    if include_image_language != "":
        _collection.load_query(include_image_language=include_image_language)
    return _collection.request()


def translations(collection_id: int) -> dict:

    _collection.reset()
    _collection.use("collection-translations")
    _collection.load_path_arg(collection_id=collection_id)
    return _collection.request()
