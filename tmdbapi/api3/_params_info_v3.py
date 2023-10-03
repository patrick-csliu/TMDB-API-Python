_ACCOUNT = {
    "account-add-favorite": {
        "description": "",
        "method": "post",
        "params": [
            {"in": "path", "name": "account_id"},
            {"in": "query", "name": "session_id"},
            {"in": "body", "name": "RAW_BODY"},
        ],
        "url": "/3/account/{account_id}/favorite",
    },
    "account-add-to-watchlist": {
        "description": "",
        "method": "post",
        "params": [
            {"in": "path", "name": "account_id"},
            {"in": "query", "name": "session_id"},
            {"in": "body", "name": "RAW_BODY"},
        ],
        "url": "/3/account/{account_id}/watchlist",
    },
    "account-details": {
        "description": "",
        "method": "get",
        "params": [
            {"in": "path", "name": "account_id"},
            {"in": "query", "name": "session_id"},
        ],
        "url": "/3/account/{account_id}",
    },
    "account-favorite-tv": {
        "description": "",
        "method": "get",
        "params": [
            {"in": "path", "name": "account_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "session_id"},
            {"in": "query", "name": "sort_by"},
        ],
        "url": "/3/account/{account_id}/favorite/tv",
    },
    "account-get-favorites": {
        "description": "",
        "method": "get",
        "params": [
            {"in": "path", "name": "account_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "session_id"},
            {"in": "query", "name": "sort_by"},
        ],
        "url": "/3/account/{account_id}/favorite/movies",
    },
    "account-lists": {
        "description": "",
        "method": "get",
        "params": [
            {"in": "path", "name": "account_id"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "session_id"},
        ],
        "url": "/3/account/{account_id}/lists",
    },
    "account-rated-movies": {
        "description": "",
        "method": "get",
        "params": [
            {"in": "path", "name": "account_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "session_id"},
            {"in": "query", "name": "sort_by"},
        ],
        "url": "/3/account/{account_id}/rated/movies",
    },
    "account-rated-tv": {
        "description": "",
        "method": "get",
        "params": [
            {"in": "path", "name": "account_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "session_id"},
            {"in": "query", "name": "sort_by"},
        ],
        "url": "/3/account/{account_id}/rated/tv",
    },
    "account-rated-tv-episodes": {
        "description": "",
        "method": "get",
        "params": [
            {"in": "path", "name": "account_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "session_id"},
            {"in": "query", "name": "sort_by"},
        ],
        "url": "/3/account/{account_id}/rated/tv/episodes",
    },
    "account-watchlist-movies": {
        "description": "",
        "method": "get",
        "params": [
            {"in": "path", "name": "account_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "session_id"},
            {"in": "query", "name": "sort_by"},
        ],
        "url": "/3/account/{account_id}/watchlist/movies",
    },
    "account-watchlist-tv": {
        "description": "",
        "method": "get",
        "params": [
            {"in": "path", "name": "account_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "session_id"},
            {"in": "query", "name": "sort_by"},
        ],
        "url": "/3/account/{account_id}/watchlist/tv",
    },
}
_AUTHENTICATION = {
    "authentication-create-guest-session": {
        "description": "",
        "method": "get",
        "params": [],
        "url": "/3/authentication/guest_session/new",
    },
    "authentication-create-request-token": {
        "description": "",
        "method": "get",
        "params": [],
        "url": "/3/authentication/token/new",
    },
    "authentication-create-session": {
        "description": "",
        "method": "post",
        "params": [{"in": "body", "name": "RAW_BODY"}],
        "url": "/3/authentication/session/new",
    },
    "authentication-create-session-from-login": {
        "description": "This method "
        "allows an "
        "application to "
        "validate a "
        "request token by "
        "entering a "
        "username and "
        "password.",
        "method": "post",
        "params": [{"in": "body", "name": "RAW_BODY"}],
        "url": "/3/authentication/token/validate_with_login",
    },
    "authentication-create-session-from-v4-token": {
        "description": "",
        "method": "post",
        "params": [{"in": "body", "name": "RAW_BODY"}],
        "url": "/3/authentication/session/convert/4",
    },
    "authentication-delete-session": {
        "description": "",
        "method": "delete",
        "params": [{"in": "body", "name": "RAW_BODY"}],
        "url": "/3/authentication/session",
    },
    "authentication-validate-key": {
        "description": "Test your API Key to see if " "it's valid.",
        "method": "get",
        "params": [],
        "url": "/3/authentication",
    },
}
_CERTIFICATIONS = {
    "certification-movie-list": {
        "description": "Get an up to date list of the "
        "officially supported movie "
        "certifications on TMDB.",
        "method": "get",
        "params": [],
        "url": "/3/certification/movie/list",
    },
    "certifications-tv-list": {
        "description": "",
        "method": "get",
        "params": [],
        "url": "/3/certification/tv/list",
    },
}
_CHANGES = {
    "changes-movie-list": {
        "description": "Get a list of all of the movie ids "
        "that have been changed in the past 24 "
        "hours.",
        "method": "get",
        "params": [
            {"in": "query", "name": "end_date"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "start_date"},
        ],
        "url": "/3/movie/changes",
    },
    "changes-people-list": {
        "description": "",
        "method": "get",
        "params": [
            {"in": "query", "name": "end_date"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "start_date"},
        ],
        "url": "/3/person/changes",
    },
    "changes-tv-list": {
        "description": "",
        "method": "get",
        "params": [
            {"in": "query", "name": "end_date"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "start_date"},
        ],
        "url": "/3/tv/changes",
    },
}
_COLLECTIONS = {
    "collection-details": {
        "description": "Get collection details by ID.",
        "method": "get",
        "params": [
            {"in": "path", "name": "collection_id"},
            {"in": "query", "name": "language"},
        ],
        "url": "/3/collection/{collection_id}",
    },
    "collection-images": {
        "description": "Get the images that belong to a " "collection.",
        "method": "get",
        "params": [
            {"in": "path", "name": "collection_id"},
            {"in": "query", "name": "include_image_language"},
            {"in": "query", "name": "language"},
        ],
        "url": "/3/collection/{collection_id}/images",
    },
    "collection-translations": {
        "description": "",
        "method": "get",
        "params": [{"in": "path", "name": "collection_id"}],
        "url": "/3/collection/{collection_id}/translations",
    },
}
_COMPANIES = {
    "company-alternative-names": {
        "description": "Get the company details by ID.",
        "method": "get",
        "params": [{"in": "path", "name": "company_id"}],
        "url": "/3/company/{company_id}/alternative_names",
    },
    "company-details": {
        "description": "Get the company details by ID.",
        "method": "get",
        "params": [{"in": "path", "name": "company_id"}],
        "url": "/3/company/{company_id}",
    },
    "company-images": {
        "description": "Get the company logos by id.",
        "method": "get",
        "params": [{"in": "path", "name": "company_id"}],
        "url": "/3/company/{company_id}/images",
    },
}
_CONFIGURATION = {
    "configuration-countries": {
        "description": "Get the list of countries (ISO "
        "3166-1 tags) used throughout "
        "TMDB.",
        "method": "get",
        "params": [{"in": "query", "name": "language"}],
        "url": "/3/configuration/countries",
    },
    "configuration-details": {
        "description": "Query the API configuration " "details.",
        "method": "get",
        "params": [],
        "url": "/3/configuration",
    },
    "configuration-jobs": {
        "description": "Get the list of the jobs and " "departments we use on TMDB.",
        "method": "get",
        "params": [],
        "url": "/3/configuration/jobs",
    },
    "configuration-languages": {
        "description": "Get the list of languages (ISO "
        "639-1 tags) used throughout TMDB.",
        "method": "get",
        "params": [],
        "url": "/3/configuration/languages",
    },
    "configuration-primary-translations": {
        "description": "Get a list of the "
        "officially supported "
        "translations on TMDB.",
        "method": "get",
        "params": [],
        "url": "/3/configuration/primary_translations",
    },
    "configuration-timezones": {
        "description": "Get the list of timezones used " "throughout TMDB.",
        "method": "get",
        "params": [],
        "url": "/3/configuration/timezones",
    },
}
_CREDITS = {
    "credit-details": {
        "description": "Get a movie or TV credit details by ID.",
        "method": "get",
        "params": [{"in": "path", "name": "credit_id"}],
        "url": "/3/credit/{credit_id}",
    }
}
_DISCOVER = {
    "discover-movie": {
        "description": "Find movies using over 30 filters and sort " "options.",
        "method": "get",
        "params": [
            {"in": "query", "name": "certification"},
            {"in": "query", "name": "certification.gte"},
            {"in": "query", "name": "certification.lte"},
            {"in": "query", "name": "certification_country"},
            {"in": "query", "name": "include_adult"},
            {"in": "query", "name": "include_video"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "primary_release_year"},
            {"in": "query", "name": "primary_release_date.gte"},
            {"in": "query", "name": "primary_release_date.lte"},
            {"in": "query", "name": "region"},
            {"in": "query", "name": "release_date.gte"},
            {"in": "query", "name": "release_date.lte"},
            {"in": "query", "name": "sort_by"},
            {"in": "query", "name": "vote_average.gte"},
            {"in": "query", "name": "vote_average.lte"},
            {"in": "query", "name": "vote_count.gte"},
            {"in": "query", "name": "vote_count.lte"},
            {"in": "query", "name": "watch_region"},
            {"in": "query", "name": "with_cast"},
            {"in": "query", "name": "with_companies"},
            {"in": "query", "name": "with_crew"},
            {"in": "query", "name": "with_genres"},
            {"in": "query", "name": "with_keywords"},
            {"in": "query", "name": "with_origin_country"},
            {"in": "query", "name": "with_original_language"},
            {"in": "query", "name": "with_people"},
            {"in": "query", "name": "with_release_type"},
            {"in": "query", "name": "with_runtime.gte"},
            {"in": "query", "name": "with_runtime.lte"},
            {"in": "query", "name": "with_watch_monetization_types"},
            {"in": "query", "name": "with_watch_providers"},
            {"in": "query", "name": "without_companies"},
            {"in": "query", "name": "without_genres"},
            {"in": "query", "name": "without_keywords"},
            {"in": "query", "name": "without_watch_providers"},
            {"in": "query", "name": "year"},
        ],
        "url": "/3/discover/movie",
    },
    "discover-tv": {
        "description": "Find TV shows using over 30 filters and sort " "options.",
        "method": "get",
        "params": [
            {"in": "query", "name": "air_date.gte"},
            {"in": "query", "name": "air_date.lte"},
            {"in": "query", "name": "first_air_date_year"},
            {"in": "query", "name": "first_air_date.gte"},
            {"in": "query", "name": "first_air_date.lte"},
            {"in": "query", "name": "include_adult"},
            {"in": "query", "name": "include_null_first_air_dates"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "screened_theatrically"},
            {"in": "query", "name": "sort_by"},
            {"in": "query", "name": "timezone"},
            {"in": "query", "name": "vote_average.gte"},
            {"in": "query", "name": "vote_average.lte"},
            {"in": "query", "name": "vote_count.gte"},
            {"in": "query", "name": "vote_count.lte"},
            {"in": "query", "name": "watch_region"},
            {"in": "query", "name": "with_companies"},
            {"in": "query", "name": "with_genres"},
            {"in": "query", "name": "with_keywords"},
            {"in": "query", "name": "with_networks"},
            {"in": "query", "name": "with_origin_country"},
            {"in": "query", "name": "with_original_language"},
            {"in": "query", "name": "with_runtime.gte"},
            {"in": "query", "name": "with_runtime.lte"},
            {"in": "query", "name": "with_status"},
            {"in": "query", "name": "with_watch_monetization_types"},
            {"in": "query", "name": "with_watch_providers"},
            {"in": "query", "name": "without_companies"},
            {"in": "query", "name": "without_genres"},
            {"in": "query", "name": "without_keywords"},
            {"in": "query", "name": "without_watch_providers"},
            {"in": "query", "name": "with_type"},
        ],
        "url": "/3/discover/tv",
    },
}
_FIND = {
    "find-by-id": {
        "description": "Find data by external ID's.",
        "method": "get",
        "params": [
            {"in": "path", "name": "external_id"},
            {"in": "query", "name": "external_source"},
            {"in": "query", "name": "language"},
        ],
        "url": "/3/find/{external_id}",
    }
}
_GENRES = {
    "genre-movie-list": {
        "description": "Get the list of official genres for " "movies.",
        "method": "get",
        "params": [{"in": "query", "name": "language"}],
        "url": "/3/genre/movie/list",
    },
    "genre-tv-list": {
        "description": "Get the list of official genres for TV " "shows.",
        "method": "get",
        "params": [{"in": "query", "name": "language"}],
        "url": "/3/genre/tv/list",
    },
}
_GUEST_SESSIONS = {
    "guest-session-rated-movies": {
        "description": "Get the rated movies for a " "guest session.",
        "method": "get",
        "params": [
            {"in": "path", "name": "guest_session_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "sort_by"},
        ],
        "url": "/3/guest_session/{guest_session_id}/rated/movies",
    },
    "guest-session-rated-tv": {
        "description": "Get the rated TV shows for a guest " "session.",
        "method": "get",
        "params": [
            {"in": "path", "name": "guest_session_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "sort_by"},
        ],
        "url": "/3/guest_session/{guest_session_id}/rated/tv",
    },
    "guest-session-rated-tv-episodes": {
        "description": "Get the rated TV episodes " "for a guest session.",
        "method": "get",
        "params": [
            {"in": "path", "name": "guest_session_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "sort_by"},
        ],
        "url": "/3/guest_session/{guest_session_id}/rated/tv/episodes",
    },
}
_KEYWORDS = {
    "keyword-details": {
        "description": "",
        "method": "get",
        "params": [{"in": "path", "name": "keyword_id"}],
        "url": "/3/keyword/{keyword_id}",
    },
    "keyword-movies": {
        "description": "",
        "method": "get",
        "params": [
            {"in": "path", "name": "keyword_id"},
            {"in": "query", "name": "include_adult"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
        ],
        "url": "/3/keyword/{keyword_id}/movies",
    },
}
_LISTS = {
    "list-add-movie": {
        "description": "Add a movie to a list.",
        "method": "post",
        "params": [
            {"in": "path", "name": "list_id"},
            {"in": "query", "name": "session_id"},
            {"in": "body", "name": "RAW_BODY"},
        ],
        "url": "/3/list/{list_id}/add_item",
    },
    "list-check-item-status": {
        "description": "Use this method to check if an "
        "item has already been added to the "
        "list.",
        "method": "get",
        "params": [
            {"in": "path", "name": "list_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "movie_id"},
        ],
        "url": "/3/list/{list_id}/item_status",
    },
    "list-clear": {
        "description": "Clear all items from a list.",
        "method": "post",
        "params": [
            {"in": "path", "name": "list_id"},
            {"in": "query", "name": "session_id"},
            {"in": "query", "name": "confirm"},
        ],
        "url": "/3/list/{list_id}/clear",
    },
    "list-create": {
        "description": "",
        "method": "post",
        "params": [
            {"in": "query", "name": "session_id"},
            {"in": "body", "name": "RAW_BODY"},
        ],
        "url": "/3/list",
    },
    "list-delete": {
        "description": "Delete a list.",
        "method": "delete",
        "params": [
            {"in": "path", "name": "list_id"},
            {"in": "query", "name": "session_id"},
        ],
        "url": "/3/list/{list_id}",
    },
    "list-details": {
        "description": "",
        "method": "get",
        "params": [
            {"in": "path", "name": "list_id"},
            {"in": "query", "name": "language"},
        ],
        "url": "/3/list/{list_id}",
    },
    "list-remove-movie": {
        "description": "Remove a movie from a list.",
        "method": "post",
        "params": [
            {"in": "path", "name": "list_id"},
            {"in": "query", "name": "session_id"},
            {"in": "body", "name": "RAW_BODY"},
        ],
        "url": "/3/list/{list_id}/remove_item",
    },
}
_MOVIE_LISTS = {
    "movie-now-playing-list": {
        "description": "Get a list of movies that are " "currently in theatres.",
        "method": "get",
        "params": [
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "region"},
        ],
        "url": "/3/movie/now_playing",
    },
    "movie-popular-list": {
        "description": "Get a list of movies ordered by " "popularity.",
        "method": "get",
        "params": [
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "region"},
        ],
        "url": "/3/movie/popular",
    },
    "movie-top-rated-list": {
        "description": "Get a list of movies ordered by " "rating.",
        "method": "get",
        "params": [
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "region"},
        ],
        "url": "/3/movie/top_rated",
    },
    "movie-upcoming-list": {
        "description": "Get a list of movies that are being " "released soon.",
        "method": "get",
        "params": [
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "region"},
        ],
        "url": "/3/movie/upcoming",
    },
}
_MOVIES = {
    "movie-account-states": {
        "description": "Get the rating, watchlist and "
        "favourite status of an account.",
        "method": "get",
        "params": [
            {"in": "path", "name": "movie_id"},
            {"in": "query", "name": "session_id"},
            {"in": "query", "name": "guest_session_id"},
        ],
        "url": "/3/movie/{movie_id}/account_states",
    },
    "movie-add-rating": {
        "description": "Rate a movie and save it to your rated " "list.",
        "method": "post",
        "params": [
            {"in": "path", "name": "movie_id"},
            {"in": "query", "name": "guest_session_id"},
            {"in": "query", "name": "session_id"},
            {"in": "body", "name": "RAW_BODY"},
            {"in": "header", "name": "Content-Type"},
        ],
        "url": "/3/movie/{movie_id}/rating",
    },
    "movie-alternative-titles": {
        "description": "Get the alternative titles for a " "movie.",
        "method": "get",
        "params": [
            {"in": "path", "name": "movie_id"},
            {"in": "query", "name": "country"},
        ],
        "url": "/3/movie/{movie_id}/alternative_titles",
    },
    "movie-changes": {
        "description": "Get the recent changes for a movie.",
        "method": "get",
        "params": [
            {"in": "path", "name": "movie_id"},
            {"in": "query", "name": "end_date"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "start_date"},
        ],
        "url": "/3/movie/{movie_id}/changes",
    },
    "movie-credits": {
        "description": "",
        "method": "get",
        "params": [
            {"in": "path", "name": "movie_id"},
            {"in": "query", "name": "language"},
        ],
        "url": "/3/movie/{movie_id}/credits",
    },
    "movie-delete-rating": {
        "description": "Delete a user rating.",
        "method": "delete",
        "params": [
            {"in": "path", "name": "movie_id"},
            {"in": "header", "name": "Content-Type"},
            {"in": "query", "name": "guest_session_id"},
            {"in": "query", "name": "session_id"},
        ],
        "url": "/3/movie/{movie_id}/rating",
    },
    "movie-details": {
        "description": "Get the top level details of a movie by ID.",
        "method": "get",
        "params": [
            {"in": "path", "name": "movie_id"},
            {"in": "query", "name": "append_to_response"},
            {"in": "query", "name": "language"},
        ],
        "url": "/3/movie/{movie_id}",
    },
    "movie-external-ids": {
        "description": "",
        "method": "get",
        "params": [{"in": "path", "name": "movie_id"}],
        "url": "/3/movie/{movie_id}/external_ids",
    },
    "movie-images": {
        "description": "Get the images that belong to a movie.",
        "method": "get",
        "params": [
            {"in": "path", "name": "movie_id"},
            {"in": "query", "name": "include_image_language"},
            {"in": "query", "name": "language"},
        ],
        "url": "/3/movie/{movie_id}/images",
    },
    "movie-keywords": {
        "description": "",
        "method": "get",
        "params": [{"in": "path", "name": "movie_id"}],
        "url": "/3/movie/{movie_id}/keywords",
    },
    "movie-latest-id": {
        "description": "Get the newest movie ID.",
        "method": "get",
        "params": [],
        "url": "/3/movie/latest",
    },
    "movie-lists": {
        "description": "",
        "method": "get",
        "params": [
            {"in": "path", "name": "movie_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
        ],
        "url": "/3/movie/{movie_id}/lists",
    },
    "movie-recommendations": {
        "description": "",
        "method": "get",
        "params": [
            {"in": "path", "name": "movie_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
        ],
        "url": "/3/movie/{movie_id}/recommendations",
    },
    "movie-release-dates": {
        "description": "Get the release dates and " "certifications for a movie.",
        "method": "get",
        "params": [{"in": "path", "name": "movie_id"}],
        "url": "/3/movie/{movie_id}/release_dates",
    },
    "movie-reviews": {
        "description": "Get the user reviews for a movie.",
        "method": "get",
        "params": [
            {"in": "path", "name": "movie_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
        ],
        "url": "/3/movie/{movie_id}/reviews",
    },
    "movie-similar": {
        "description": "Get the similar movies based on genres and " "keywords.",
        "method": "get",
        "params": [
            {"in": "path", "name": "movie_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
        ],
        "url": "/3/movie/{movie_id}/similar",
    },
    "movie-translations": {
        "description": "Get the translations for a movie.",
        "method": "get",
        "params": [{"in": "path", "name": "movie_id"}],
        "url": "/3/movie/{movie_id}/translations",
    },
    "movie-videos": {
        "description": "",
        "method": "get",
        "params": [
            {"in": "path", "name": "movie_id"},
            {"in": "query", "name": "language"},
        ],
        "url": "/3/movie/{movie_id}/videos",
    },
    "movie-watch-providers": {
        "description": "Get the list of streaming providers " "we have for a movie.",
        "method": "get",
        "params": [{"in": "path", "name": "movie_id"}],
        "url": "/3/movie/{movie_id}/watch/providers",
    },
}
_NETWORKS = {
    "alternative-names-copy": {
        "description": "Get the TV network logos by id.",
        "method": "get",
        "params": [{"in": "path", "name": "network_id"}],
        "url": "/3/network/{network_id}/images",
    },
    "details-copy": {
        "description": "Get the alternative names of a network.",
        "method": "get",
        "params": [{"in": "path", "name": "network_id"}],
        "url": "/3/network/{network_id}/alternative_names",
    },
    "network-details": {
        "description": "",
        "method": "get",
        "params": [{"in": "path", "name": "network_id"}],
        "url": "/3/network/{network_id}",
    },
}
_PEOPLE_LISTS = {
    "person-popular-list": {
        "description": "Get a list of people ordered by " "popularity.",
        "method": "get",
        "params": [
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
        ],
        "url": "/3/person/popular",
    }
}
_PEOPLE = {
    "person-changes": {
        "description": "Get the recent changes for a person.",
        "method": "get",
        "params": [
            {"in": "path", "name": "person_id"},
            {"in": "query", "name": "end_date"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "start_date"},
        ],
        "url": "/3/person/{person_id}/changes",
    },
    "person-combined-credits": {
        "description": "Get the combined movie and TV "
        "credits that belong to a person.",
        "method": "get",
        "params": [
            {"in": "path", "name": "person_id"},
            {"in": "query", "name": "language"},
        ],
        "url": "/3/person/{person_id}/combined_credits",
    },
    "person-details": {
        "description": "Query the top level details of a person.",
        "method": "get",
        "params": [
            {"in": "path", "name": "person_id"},
            {"in": "query", "name": "append_to_response"},
            {"in": "query", "name": "language"},
        ],
        "url": "/3/person/{person_id}",
    },
    "person-external-ids": {
        "description": "Get the external ID's that belong to " "a person.",
        "method": "get",
        "params": [{"in": "path", "name": "person_id"}],
        "url": "/3/person/{person_id}/external_ids",
    },
    "person-images": {
        "description": "Get the profile images that belong to a " "person.",
        "method": "get",
        "params": [{"in": "path", "name": "person_id"}],
        "url": "/3/person/{person_id}/images",
    },
    "person-latest-id": {
        "description": "Get the newest created person. This is a "
        "live response and will continuously "
        "change.",
        "method": "get",
        "params": [],
        "url": "/3/person/latest",
    },
    "person-movie-credits": {
        "description": "Get the movie credits for a person.",
        "method": "get",
        "params": [
            {"in": "path", "name": "person_id"},
            {"in": "query", "name": "language"},
        ],
        "url": "/3/person/{person_id}/movie_credits",
    },
    "person-tagged-images": {
        "description": "Get the tagged images for a person.",
        "method": "get",
        "params": [
            {"in": "path", "name": "person_id"},
            {"in": "query", "name": "page"},
        ],
        "url": "/3/person/{person_id}/tagged_images",
    },
    "person-tv-credits": {
        "description": "Get the TV credits that belong to a " "person.",
        "method": "get",
        "params": [
            {"in": "path", "name": "person_id"},
            {"in": "query", "name": "language"},
        ],
        "url": "/3/person/{person_id}/tv_credits",
    },
    "translations": {
        "description": "Get the translations that belong to a " "person.",
        "method": "get",
        "params": [{"in": "path", "name": "person_id"}],
        "url": "/3/person/{person_id}/translations",
    },
}
_REVIEWS = {
    "review-details": {
        "description": "Retrieve the details of a movie or TV show " "review.",
        "method": "get",
        "params": [{"in": "path", "name": "review_id"}],
        "url": "/3/review/{review_id}",
    }
}
_SEARCH = {
    "search-collection": {
        "description": "Search for collections by their "
        "original, translated and alternative "
        "names.",
        "method": "get",
        "params": [
            {"in": "query", "name": "query"},
            {"in": "query", "name": "include_adult"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "region"},
        ],
        "url": "/3/search/collection",
    },
    "search-company": {
        "description": "Search for companies by their original and "
        "alternative names.",
        "method": "get",
        "params": [{"in": "query", "name": "query"}, {"in": "query", "name": "page"}],
        "url": "/3/search/company",
    },
    "search-keyword": {
        "description": "Search for keywords by their name.",
        "method": "get",
        "params": [{"in": "query", "name": "query"}, {"in": "query", "name": "page"}],
        "url": "/3/search/keyword",
    },
    "search-movie": {
        "description": "Search for movies by their original, "
        "translated and alternative titles.",
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
        "url": "/3/search/movie",
    },
    "search-multi": {
        "description": "Use multi search when you want to search for "
        "movies, TV shows and people in a single "
        "request.",
        "method": "get",
        "params": [
            {"in": "query", "name": "query"},
            {"in": "query", "name": "include_adult"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
        ],
        "url": "/3/search/multi",
    },
    "search-person": {
        "description": "Search for people by their name and also " "known as names.",
        "method": "get",
        "params": [
            {"in": "query", "name": "query"},
            {"in": "query", "name": "include_adult"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
        ],
        "url": "/3/search/person",
    },
    "search-tv": {
        "description": "Search for TV shows by their original, "
        "translated and also known as names.",
        "method": "get",
        "params": [
            {"in": "query", "name": "query"},
            {"in": "query", "name": "first_air_date_year"},
            {"in": "query", "name": "include_adult"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "year"},
        ],
        "url": "/3/search/tv",
    },
}
_TRENDING = {
    "trending-all": {
        "description": "Get the trending movies, TV shows and " "people.",
        "method": "get",
        "params": [
            {"in": "path", "name": "time_window"},
            {"in": "query", "name": "language"},
        ],
        "url": "/3/trending/all/{time_window}",
    },
    "trending-movies": {
        "description": "Get the trending movies on TMDB.",
        "method": "get",
        "params": [
            {"in": "path", "name": "time_window"},
            {"in": "query", "name": "language"},
        ],
        "url": "/3/trending/movie/{time_window}",
    },
    "trending-people": {
        "description": "Get the trending people on TMDB.",
        "method": "get",
        "params": [
            {"in": "path", "name": "time_window"},
            {"in": "query", "name": "language"},
        ],
        "url": "/3/trending/person/{time_window}",
    },
    "trending-tv": {
        "description": "Get the trending TV shows on TMDB.",
        "method": "get",
        "params": [
            {"in": "path", "name": "time_window"},
            {"in": "query", "name": "language"},
        ],
        "url": "/3/trending/tv/{time_window}",
    },
}
_TV_SERIES_LISTS = {
    "tv-series-airing-today-list": {
        "description": "Get a list of TV shows airing " "today.",
        "method": "get",
        "params": [
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "timezone"},
        ],
        "url": "/3/tv/airing_today",
    },
    "tv-series-on-the-air-list": {
        "description": "Get a list of TV shows that air " "in the next 7 days.",
        "method": "get",
        "params": [
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "timezone"},
        ],
        "url": "/3/tv/on_the_air",
    },
    "tv-series-popular-list": {
        "description": "Get a list of TV shows ordered by " "popularity.",
        "method": "get",
        "params": [
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
        ],
        "url": "/3/tv/popular",
    },
    "tv-series-top-rated-list": {
        "description": "Get a list of TV shows ordered " "by rating.",
        "method": "get",
        "params": [
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
        ],
        "url": "/3/tv/top_rated",
    },
}
_TV_SERIES = {
    "tv-series-account-states": {
        "description": "Get the rating, watchlist and " "favourite status.",
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "session_id"},
            {"in": "query", "name": "guest_session_id"},
        ],
        "url": "/3/tv/{series_id}/account_states",
    },
    "tv-series-add-rating": {
        "description": "Rate a TV show and save it to your " "rated list.",
        "method": "post",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "guest_session_id"},
            {"in": "query", "name": "session_id"},
            {"in": "body", "name": "RAW_BODY"},
            {"in": "header", "name": "Content-Type"},
        ],
        "url": "/3/tv/{series_id}/rating",
    },
    "tv-series-aggregate-credits": {
        "description": "Get the aggregate credits "
        "(cast and crew) that have "
        "been added to a TV show.",
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "language"},
        ],
        "url": "/3/tv/{series_id}/aggregate_credits",
    },
    "tv-series-alternative-titles": {
        "description": "Get the alternative titles "
        "that have been added to a TV "
        "show.",
        "method": "get",
        "params": [{"in": "path", "name": "series_id"}],
        "url": "/3/tv/{series_id}/alternative_titles",
    },
    "tv-series-changes": {
        "description": "Get the recent changes for a TV show.",
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "end_date"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "start_date"},
        ],
        "url": "/3/tv/{series_id}/changes",
    },
    "tv-series-content-ratings": {
        "description": "Get the content ratings that " "have been added to a TV show.",
        "method": "get",
        "params": [{"in": "path", "name": "series_id"}],
        "url": "/3/tv/{series_id}/content_ratings",
    },
    "tv-series-credits": {
        "description": "Get the latest season credits of a TV " "show.",
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "language"},
        ],
        "url": "/3/tv/{series_id}/credits",
    },
    "tv-series-delete-rating": {
        "description": "",
        "method": "delete",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "header", "name": "Content-Type"},
            {"in": "query", "name": "guest_session_id"},
            {"in": "query", "name": "session_id"},
        ],
        "url": "/3/tv/{series_id}/rating",
    },
    "tv-series-details": {
        "description": "Get the details of a TV show.",
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "append_to_response"},
            {"in": "query", "name": "language"},
        ],
        "url": "/3/tv/{series_id}",
    },
    "tv-series-episode-groups": {
        "description": "Get the episode groups that have " "been added to a TV show.",
        "method": "get",
        "params": [{"in": "path", "name": "series_id"}],
        "url": "/3/tv/{series_id}/episode_groups",
    },
    "tv-series-external-ids": {
        "description": "Get a list of external IDs that "
        "have been added to a TV show.",
        "method": "get",
        "params": [{"in": "path", "name": "series_id"}],
        "url": "/3/tv/{series_id}/external_ids",
    },
    "tv-series-images": {
        "description": "Get the images that belong to a TV " "series.",
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "include_image_language"},
            {"in": "query", "name": "language"},
        ],
        "url": "/3/tv/{series_id}/images",
    },
    "tv-series-keywords": {
        "description": "Get a list of keywords that have been " "added to a TV show.",
        "method": "get",
        "params": [{"in": "path", "name": "series_id"}],
        "url": "/3/tv/{series_id}/keywords",
    },
    "tv-series-latest-id": {
        "description": "Get the newest TV show ID.",
        "method": "get",
        "params": [],
        "url": "/3/tv/latest",
    },
    "tv-series-recommendations": {
        "description": "",
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
        ],
        "url": "/3/tv/{series_id}/recommendations",
    },
    "tv-series-reviews": {
        "description": "Get the reviews that have been added to " "a TV show.",
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
        ],
        "url": "/3/tv/{series_id}/reviews",
    },
    "tv-series-screened-theatrically": {
        "description": "Get the seasons and "
        "episodes that have "
        "screened theatrically.",
        "method": "get",
        "params": [{"in": "path", "name": "series_id"}],
        "url": "/3/tv/{series_id}/screened_theatrically",
    },
    "tv-series-similar": {
        "description": "Get the similar TV shows.",
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "language"},
            {"in": "query", "name": "page"},
        ],
        "url": "/3/tv/{series_id}/similar",
    },
    "tv-series-translations": {
        "description": "Get the translations that have " "been added to a TV show.",
        "method": "get",
        "params": [{"in": "path", "name": "series_id"}],
        "url": "/3/tv/{series_id}/translations",
    },
    "tv-series-videos": {
        "description": "Get the videos that belong to a TV show.",
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "include_video_language"},
            {"in": "query", "name": "language"},
        ],
        "url": "/3/tv/{series_id}/videos",
    },
    "tv-series-watch-providers": {
        "description": "Get the list of streaming "
        "providers we have for a TV "
        "show.",
        "method": "get",
        "params": [{"in": "path", "name": "series_id"}],
        "url": "/3/tv/{series_id}/watch/providers",
    },
}
_TV_SEASONS = {
    "tv-season-account-states": {
        "description": "Get the rating, watchlist and " "favourite status.",
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "session_id"},
            {"in": "query", "name": "guest_session_id"},
            {"in": "path", "name": "season_number"},
        ],
        "url": "/3/tv/{series_id}/season/{season_number}/account_states",
    },
    "tv-season-aggregate-credits": {
        "description": "Get the aggregate credits "
        "(cast and crew) that have "
        "been added to a TV season.",
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "language"},
            {"in": "path", "name": "season_number"},
        ],
        "url": "/3/tv/{series_id}/season/{season_number}/aggregate_credits",
    },
    "tv-season-changes-by-id": {
        "description": "Get the recent changes for a TV " "season.",
        "method": "get",
        "params": [
            {"in": "query", "name": "end_date"},
            {"in": "query", "name": "page"},
            {"in": "query", "name": "start_date"},
            {"in": "path", "name": "season_id"},
        ],
        "url": "/3/tv/season/{season_id}/changes",
    },
    "tv-season-credits": {
        "description": "",
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "path", "name": "season_number"},
            {"in": "query", "name": "language"},
        ],
        "url": "/3/tv/{series_id}/season/{season_number}/credits",
    },
    "tv-season-details": {
        "description": "Query the details of a TV season.",
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "path", "name": "season_number"},
            {"in": "query", "name": "append_to_response"},
            {"in": "query", "name": "language"},
        ],
        "url": "/3/tv/{series_id}/season/{season_number}",
    },
    "tv-season-external-ids": {
        "description": "Get a list of external IDs that "
        "have been added to a TV season.",
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "path", "name": "season_number"},
        ],
        "url": "/3/tv/{series_id}/season/{season_number}/external_ids",
    },
    "tv-season-images": {
        "description": "Get the images that belong to a TV " "season.",
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "include_image_language"},
            {"in": "query", "name": "language"},
            {"in": "path", "name": "season_number"},
        ],
        "url": "/3/tv/{series_id}/season/{season_number}/images",
    },
    "tv-season-translations": {
        "description": "Get the translations for a TV " "season.",
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "path", "name": "season_number"},
        ],
        "url": "/3/tv/{series_id}/season/{season_number}/translations",
    },
    "tv-season-videos": {
        "description": "Get the videos that belong to a TV " "season.",
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "include_video_language"},
            {"in": "query", "name": "language"},
            {"in": "path", "name": "season_number"},
        ],
        "url": "/3/tv/{series_id}/season/{season_number}/videos",
    },
    "tv-season-watch-providers": {
        "description": "Get the list of streaming "
        "providers we have for a TV "
        "season.",
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "language"},
            {"in": "path", "name": "season_number"},
        ],
        "url": "/3/tv/{series_id}/season/{season_number}/watch/providers",
    },
}
_TV_EPISODES = {
    "tv-episode-account-states": {
        "description": "Get the rating, watchlist and " "favourite status.",
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "session_id"},
            {"in": "path", "name": "season_number"},
            {"in": "path", "name": "episode_number"},
            {"in": "query", "name": "guest_session_id"},
        ],
        "url": "/3/tv/{series_id}/season/{season_number}/episode/{episode_number}/account_states",
    },
    "tv-episode-add-rating": {
        "description": "Rate a TV episode and save it to " "your rated list.",
        "method": "post",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "guest_session_id"},
            {"in": "query", "name": "session_id"},
            {"in": "body", "name": "RAW_BODY"},
            {"in": "header", "name": "Content-Type"},
            {"in": "path", "name": "season_number"},
            {"in": "path", "name": "episode_number"},
        ],
        "url": "/3/tv/{series_id}/season/{season_number}/episode/{episode_number}/rating",
    },
    "tv-episode-changes-by-id": {
        "description": "Get the recent changes for a TV " "episode.",
        "method": "get",
        "params": [{"in": "path", "name": "episode_id"}],
        "url": "/3/tv/episode/{episode_id}/changes",
    },
    "tv-episode-credits": {
        "description": "",
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "path", "name": "season_number"},
            {"in": "query", "name": "language"},
            {"in": "path", "name": "episode_number"},
        ],
        "url": "/3/tv/{series_id}/season/{season_number}/episode/{episode_number}/credits",
    },
    "tv-episode-delete-rating": {
        "description": "Delete your rating on a TV " "episode.",
        "method": "delete",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "header", "name": "Content-Type"},
            {"in": "query", "name": "guest_session_id"},
            {"in": "query", "name": "session_id"},
            {"in": "path", "name": "season_number"},
            {"in": "path", "name": "episode_number"},
        ],
        "url": "/3/tv/{series_id}/season/{season_number}/episode/{episode_number}/rating",
    },
    "tv-episode-details": {
        "description": "Query the details of a TV episode.",
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "path", "name": "season_number"},
            {"in": "path", "name": "episode_number"},
            {"in": "query", "name": "append_to_response"},
            {"in": "query", "name": "language"},
        ],
        "url": "/3/tv/{series_id}/season/{season_number}/episode/{episode_number}",
    },
    "tv-episode-external-ids": {
        "description": "Get a list of external IDs that "
        "have been added to a TV episode.",
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "path", "name": "season_number"},
            {"in": "path", "name": "episode_number"},
        ],
        "url": "/3/tv/{series_id}/season/{season_number}/episode/{episode_number}/external_ids",
    },
    "tv-episode-images": {
        "description": "Get the images that belong to a TV " "episode.",
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "include_image_language"},
            {"in": "query", "name": "language"},
            {"in": "path", "name": "season_number"},
            {"in": "path", "name": "episode_number"},
        ],
        "url": "/3/tv/{series_id}/season/{season_number}/episode/{episode_number}/images",
    },
    "tv-episode-translations": {
        "description": "Get the translations that have " "been added to a TV episode.",
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "path", "name": "season_number"},
            {"in": "path", "name": "episode_number"},
        ],
        "url": "/3/tv/{series_id}/season/{season_number}/episode/{episode_number}/translations",
    },
    "tv-episode-videos": {
        "description": "Get the videos that belong to a TV " "episode.",
        "method": "get",
        "params": [
            {"in": "path", "name": "series_id"},
            {"in": "query", "name": "include_video_language"},
            {"in": "query", "name": "language"},
            {"in": "path", "name": "season_number"},
            {"in": "path", "name": "episode_number"},
        ],
        "url": "/3/tv/{series_id}/season/{season_number}/episode/{episode_number}/videos",
    },
}
_TV_EPISODE_GROUPS = {
    "tv-episode-group-details": {
        "description": "Get the details of a TV episode " "group.",
        "method": "get",
        "params": [{"in": "path", "name": "tv_episode_group_id"}],
        "url": "/3/tv/episode_group/{tv_episode_group_id}",
    }
}
_WATCH_PROVIDERS = {
    "watch-provider-tv-list": {
        "description": "Get the list of streaming " "providers we have for TV shows.",
        "method": "get",
        "params": [
            {"in": "query", "name": "language"},
            {"in": "query", "name": "watch_region"},
        ],
        "url": "/3/watch/providers/tv",
    },
    "watch-providers-available-regions": {
        "description": "Get the list of the "
        "countries we have watch "
        "provider "
        "(OTT/streaming) data "
        "for.",
        "method": "get",
        "params": [{"in": "query", "name": "language"}],
        "url": "/3/watch/providers/regions",
    },
    "watch-providers-movie-list": {
        "description": "Get the list of streaming " "providers we have for movies.",
        "method": "get",
        "params": [
            {"in": "query", "name": "language"},
            {"in": "query", "name": "watch_region"},
        ],
        "url": "/3/watch/providers/movie",
    },
}
