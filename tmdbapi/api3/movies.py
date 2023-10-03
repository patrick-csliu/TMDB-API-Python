"""API v3 movies category

"""

from tmdbapi._core import Tmdb
from tmdbapi.exceptions import type_checking

_MOVIES_V3 = {
    "movie-account-states": {
        "method": "get",
        "params": [
            {"in": "path", "name": "movie_id"},
            {"in": "query", "name": "session_id"},
            {"in": "query", "name": "guest_session_id"},
        ],
        "url": "/{movie_id}/account_states",
    },
    "movie-add-rating": {
        "method": "post",
        "params": [
            {"in": "path", "name": "movie_id"},
            {"in": "query", "name": "guest_session_id"},
            {"in": "query", "name": "session_id"},
            {"in": "body", "name": "RAW_BODY"},
            {"in": "header", "name": "Content-Type"},
        ],
        "url": "/{movie_id}/rating",
    },
    "movie-alternative-titles": {
        "method": "get",
        "params": [
            {"in": "path", "name": "movie_id"},
            {"in": "query", "name": "country"},
        ],
        "url": "/{movie_id}/alternative_titles",
    },
    "movie-changes": {
        "method": "get",
        "params": [
            {"in": "path", "name": "movie_id"},
            {"in": "query", "name": "end_date"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "start_date"},
        ],
        "url": "/{movie_id}/changes",
    },
    "movie-credits": {
        "method": "get",
        "params": [
            {"in": "path", "name": "movie_id"},
            {"in": "query", "name": "language"},
        ],
        "url": "/{movie_id}/credits",
    },
    "movie-delete-rating": {
        "method": "delete",
        "params": [
            {"in": "path", "name": "movie_id"},
            {"in": "header", "name": "Content-Type"},
            {"in": "query", "name": "guest_session_id"},
            {"in": "query", "name": "session_id"},
        ],
        "url": "/{movie_id}/rating",
    },
    "movie-details": {
        "method": "get",
        "params": [
            {"in": "path", "name": "movie_id"},
            {"in": "query", "name": "append_to_response"},
            {"in": "query", "name": "language"},
        ],
        "url": "/{movie_id}",
    },
    "movie-external-ids": {
        "method": "get",
        "params": [{"in": "path", "name": "movie_id"}],
        "url": "/{movie_id}/external_ids",
    },
    "movie-images": {
        "method": "get",
        "params": [
            {"in": "path", "name": "movie_id"},
            {"in": "query", "name": "include_image_language"},
            {"in": "query", "name": "language"},
        ],
        "url": "/{movie_id}/images",
    },
    "movie-keywords": {
        "method": "get",
        "params": [{"in": "path", "name": "movie_id"}],
        "url": "/{movie_id}/keywords",
    },
    "movie-latest-id": {"method": "get", "params": [], "url": "/latest"},
    "movie-lists": {
        "method": "get",
        "params": [
            {"in": "path", "name": "movie_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
        ],
        "url": "/{movie_id}/lists",
    },
    "movie-recommendations": {
        "method": "get",
        "params": [
            {"in": "path", "name": "movie_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
        ],
        "url": "/{movie_id}/recommendations",
    },
    "movie-release-dates": {
        "method": "get",
        "params": [{"in": "path", "name": "movie_id"}],
        "url": "/{movie_id}/release_dates",
    },
    "movie-reviews": {
        "method": "get",
        "params": [
            {"in": "path", "name": "movie_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
        ],
        "url": "/{movie_id}/reviews",
    },
    "movie-similar": {
        "method": "get",
        "params": [
            {"in": "path", "name": "movie_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
        ],
        "url": "/{movie_id}/similar",
    },
    "movie-translations": {
        "method": "get",
        "params": [{"in": "path", "name": "movie_id"}],
        "url": "/{movie_id}/translations",
    },
    "movie-videos": {
        "method": "get",
        "params": [
            {"in": "path", "name": "movie_id"},
            {"in": "query", "name": "language"},
        ],
        "url": "/{movie_id}/videos",
    },
    "movie-watch-providers": {
        "method": "get",
        "params": [{"in": "path", "name": "movie_id"}],
        "url": "/{movie_id}/watch/providers",
    },
}


class _Movies(Tmdb):
    def __init__(self, info_var):
        super().__init__()
        self.category_path = "/movie"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url=url,
        )


def details(
    movie_id: str,
    append_to_response="videos,trailers,images,casts,translations,keywords,release_dates",
    language: str = None,
) -> dict:
    """Get the top level details of a movie by ID."""
    movies = _Movies(_MOVIES_V3)
    movies.reset()
    movies.use("movie-details")
    movies.load_path_arg(movie_id=movie_id)
    movies.language(language)
    movies.load_query(append_to_response=append_to_response)
    return movies.request()


def account_states(movie_id: str, guest_session_id: str = None) -> dict:
    """Get the rating, watchlist and favorite status of an account."""
    movies = _Movies(_MOVIES_V3)
    movies.reset()
    movies.use("movie-account-states")
    movies.load_path_arg(movie_id=movie_id)
    movies.choose_session_id(guest_session_id)
    return movies.request()


def alternative_titles(movie_id: str, country: str = None) -> dict:
    """Get the alternative titles for a movie.

    country: format ISO-3166-1
    """
    movies = _Movies(_MOVIES_V3)
    movies.reset()
    movies.use("movie-alternative-titles")
    movies.load_path_arg(movie_id=movie_id)
    movies.load_query(country=country)
    return movies.request()


def changes(movie_id: str, start_date="", end_date="", page=1) -> dict:
    """Get the recent changes for a movie.

    `start_date` and `start_date` is lte and gte
    Format: YYYY-MM-DD
    """
    movies = _Movies(_MOVIES_V3)
    movies.reset()
    movies.use("movie-changes")
    movies.load_path_arg(movie_id=movie_id)
    if start_date != "":
        type_checking("date", start_date)
        movies.load_query(start_date=start_date)
    if end_date != "":
        type_checking("date", end_date)
        movies.load_query(end_date=end_date)
    movies.load_query(page=page)
    return movies.request()


def credits(movie_id: str, language: str = None) -> dict:
    movies = _Movies(_MOVIES_V3)
    movies.reset()
    movies.use("movie-credits")
    movies.load_path_arg(movie_id=movie_id)
    movies.language(language)
    return movies.request()


def external_ids(movie_id: str) -> dict:
    movies = _Movies(_MOVIES_V3)
    movies.reset()
    movies.use("movie-external-ids")
    movies.load_path_arg(movie_id=movie_id)
    return movies.request()


def images(
    movie_id: str, include_image_language: str = None, language: str = None
) -> dict:
    """Get the images that belong to a movie.

    include_image_language:
    specify a comma separated list of ISO-639-1 values to query,
    for example: en,null
    """
    movies = _Movies(_MOVIES_V3)
    movies.reset()
    movies.use("movie-images")
    movies.load_path_arg(movie_id=movie_id)
    movies.language(language)
    if include_image_language is not None:
        movies.load_query(include_image_language=include_image_language)
    return movies.request()


def keywords(movie_id: str) -> dict:
    movies = _Movies(_MOVIES_V3)
    movies.reset()
    movies.use("movie-keywords")
    movies.load_path_arg(movie_id=movie_id)
    return movies.request()


def latest() -> dict:
    """Get the newest movie ID."""
    movies = _Movies(_MOVIES_V3)
    movies.reset()
    movies.use("movie-latest-id")
    return movies.request()


def lists(movie_id: str, page=1, language: str = None) -> dict:
    movies = _Movies(_MOVIES_V3)
    movies.reset()
    movies.use("movie-lists")
    movies.load_path_arg(movie_id=movie_id)
    movies.language(language)
    movies.load_query(page=page)
    return movies.request()


def recommendations(movie_id: str, page=1, language: str = None) -> dict:
    movies = _Movies(_MOVIES_V3)
    movies.reset()
    movies.use("movie-recommendations")
    movies.load_path_arg(movie_id=movie_id)
    movies.language(language)
    movies.load_query(page=page)
    return movies.request()


def release_dates(movie_id: str) -> dict:
    """Get the release dates and certifications for a movie."""
    movies = _Movies(_MOVIES_V3)
    movies.reset()
    movies.use("movie-release-dates")
    movies.load_path_arg(movie_id=movie_id)
    return movies.request()


def reviews(movie_id: str, page=1, language: str = None) -> dict:
    """Get the user reviews for a movie."""
    movies = _Movies(_MOVIES_V3)
    movies.reset()
    movies.use("movie-reviews")
    movies.load_path_arg(movie_id=movie_id)
    movies.language(language)
    movies.load_query(page=page)
    return movies.request()


def similar(movie_id: str, page=1, language: str = None) -> dict:
    """Get the similar movies based on genres and " "keywords."""
    movies = _Movies(_MOVIES_V3)
    movies.reset()
    movies.use("movie-similar")
    movies.load_path_arg(movie_id=movie_id)
    movies.language(language)
    movies.load_query(page=page)
    return movies.request()


def translations(movie_id: str) -> dict:
    """Get the translations for a movie."""
    movies = _Movies(_MOVIES_V3)
    movies.reset()
    movies.use("movie-translations")
    movies.load_path_arg(movie_id=movie_id)
    return movies.request()


def videos(movie_id: str, language: str = None) -> dict:
    movies = _Movies(_MOVIES_V3)
    movies.reset()
    movies.use("movie-videos")
    movies.load_path_arg(movie_id=movie_id)
    movies.language(language)
    return movies.request()


def watch_providers(movie_id: str) -> dict:
    """Get the list of streaming providers we have for a movie."""
    movies = _Movies(_MOVIES_V3)
    movies.reset()
    movies.use("movie-watch-providers")
    movies.load_path_arg(movie_id=movie_id)
    return movies.request()


def add_rating(movie_id: str, rating: int, guest_session_id: str = None) -> dict:
    """Rate a movie and save it to your rated list.

    rating: 0~10
    """
    movies = _Movies(_MOVIES_V3)
    type_checking("rating", rating)
    movies.reset()
    movies.use("movie-add-rating")
    movies.load_path_arg(movie_id=movie_id)
    movies.choose_session_id(guest_session_id)
    movies.load_json({"value": rating})
    return movies.request()


def delete_rating(movie_id: str, guest_session_id: str = None) -> dict:
    """Delete a user rating."""
    movies = _Movies(_MOVIES_V3)
    movies.reset()
    movies.use("movie-delete-rating")
    movies.load_path_arg(movie_id=movie_id)
    movies.choose_session_id(guest_session_id)
    return movies.request()
