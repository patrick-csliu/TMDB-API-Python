"""API v3 search category

query: Use '+' between the keywords
    For more information: https://developer.themoviedb.org/docs/search-and-query-for-details
"""

from tmdbapi._core import Tmdb
from tmdbapi.exceptions import type_checking

_SEARCH_V3 = {
    "search-collection": {
        "method": "get",
        "params": [
            {"in": "query", "name": "query"},
            {"in": "query", "name": "include_adult"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "region"},
        ],
        "url": "/collection",
    },
    "search-company": {
        "method": "get",
        "params": [{"in": "query", "name": "query"}, {"in": "query", "name": "page"}],
        "url": "/company",
    },
    "search-keyword": {
        "method": "get",
        "params": [{"in": "query", "name": "query"}, {"in": "query", "name": "page"}],
        "url": "/keyword",
    },
    "search-movie": {
        "method": "get",
        "params": [
            {"in": "query", "name": "query"},
            {"in": "query", "name": "include_adult"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "primary_release_year"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "region"},
            {"in": "query", "name": "year"},
        ],
        "url": "/movie",
    },
    "search-multi": {
        "method": "get",
        "params": [
            {"in": "query", "name": "query"},
            {"in": "query", "name": "include_adult"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
        ],
        "url": "/multi",
    },
    "search-person": {
        "method": "get",
        "params": [
            {"in": "query", "name": "query"},
            {"in": "query", "name": "include_adult"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
        ],
        "url": "/person",
    },
    "search-tv": {
        "method": "get",
        "params": [
            {"in": "query", "name": "query"},
            {"in": "query", "name": "first_air_date_year"},
            {"in": "query", "name": "include_adult"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "year"},
        ],
        "url": "/tv",
    },
}


class _Search(Tmdb):
    def __init__(self, info_var):
        super().__init__()
        self.category_path = "/search"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url=url,
        )


def collections(
    query: str, include_adult=False, page=1, language: str = None, region: str = None
) -> dict:
    """Search for collections by their original, translated and
    alternative names.
    """
    search = _Search(_SEARCH_V3)
    search.reset()
    search.use("search-collection")
    search.language(language)
    search.region(region)
    search.load_query({"query": query}, include_adult=include_adult, page=page)
    return search.request()


def companies(query: str, page=1) -> dict:
    """Search for companies by their original and alternative names."""
    search = _Search(_SEARCH_V3)
    search.reset()
    search.use("search-company")
    search.load_query({"query": query}, page=page)
    return search.request()


def keywords(query: str, page=1) -> dict:
    """Search for keywords by their name."""
    search = _Search(_SEARCH_V3)
    search.reset()
    search.use("search-keyword")
    search.load_query({"query": query}, page=page)
    return search.request()


def movies(
    query: str,
    include_adult=False,
    language: str = None,
    region: str = None,
    year: str = "",
    primary_release_year: str = "",
    page=1,
) -> dict:
    """Search for movies by their original, translated and
    alternative titles.
    """
    search = _Search(_SEARCH_V3)
    search.reset()
    search.use("search-movie")
    search.language(language)
    search.region(region)
    search.load_query({"query": query}, include_adult=include_adult, page=page)
    if year != "":
        type_checking("year", year)
        search.load_query(year=year)
    if primary_release_year != "":
        type_checking("year", primary_release_year)
        search.load_query(primary_release_year=primary_release_year)
    return search.request()


def multi(query: str, include_adult=False, language: str = None, page=1) -> dict:
    """Use multi search when you want to search for movies,
    TV shows and people in a single request.
    """
    search = _Search(_SEARCH_V3)
    search.reset()
    search.use("search-multi")
    search.language(language)
    search.load_query({"query": query}, include_adult=include_adult, page=page)
    return search.request()


def person(query: str, include_adult=False, language: str = None, page=1) -> dict:
    """Search for people by their name and also " "known as names."""
    search = _Search(_SEARCH_V3)
    search.reset()
    search.use("search-person")
    search.language(language)
    search.load_query({"query": query}, include_adult=include_adult, page=page)
    return search.request()


def tv(
    query: str,
    include_adult=False,
    language: str = None,
    year: str = "",
    first_air_date_year: str = "",
    page=1,
) -> dict:
    """Search for TV shows by their original, translated and also
    known as names.
    """
    search = _Search(_SEARCH_V3)
    search.reset()
    search.use("search-tv")
    search.language(language)
    search.load_query({"query": query}, include_adult=include_adult, page=page)
    if year != "":
        type_checking("year", year)
        search.load_query(year=year)
    if first_air_date_year != "":
        type_checking("year", first_air_date_year)
        search.load_query(first_air_date_year=first_air_date_year)
    return search.request()
