"""
Exceptions and Warnings
=======================

Exceptions used by tmdbapi.

Warnings
--------

   ComplexWarning             Given when converting complex to real.
   VisibleDeprecationWarning  Same as a DeprecationWarning, but more visible.
   RankWarning                Issued when the design matrix is rank deficient.

Exceptions
----------

    AxisError          Given when an axis was invalid.
    DTypePromotionError   Given when no common dtype could be found.
    TooHardError       Error specific to `numpy.shares_memory`.

"""


__all__ = [
    "ComplexWarning", "VisibleDeprecationWarning", "ModuleDeprecationWarning",
    "TooHardError", "AxisError", "DTypePromotionError"]

_status = [
    (1, 200, 'Success.'),
    (2, 501, 'Invalid service: this service does not exist.'),
    (3, 401, 'Authentication failed: You do not have permissions to access the service.'),
    (4, 405, "Invalid format: This service doesn't exist in that format."),
    (5, 422, 'Invalid parameters: Your request parameters are incorrect.'),
    (6, 404, 'Invalid id: The pre-requisite id is invalid or not found.'),
    (7, 401, 'Invalid API key: You must be granted a valid key.'),
    (8, 403, 'Duplicate entry: The data you tried to submit already exists.'),
    (9, 503, 'Service offline: This service is temporarily offline, try again later.'),
    (10, 401, 'Suspended API key: Access to your account has been suspended, contact TMDB.'),
    (11, 500, 'Internal error: Something went wrong, contact TMDB.'),
    (12, 201, 'The item/record was updated successfully.'),
    (13, 200, 'The item/record was deleted successfully.'),
    (14, 401, 'Authentication failed.'),
    (15, 500, 'Failed.'),
    (16, 401, 'Device denied.'),
    (17, 401, 'Session denied.'),
    (18, 400, 'Validation failed.'),
    (19, 406, 'Invalid accept header.'),
    (20, 422, 'Invalid date range: Should be a range no longer than 14 days.'),
    (21, 200, 'Entry not found: The item you are trying to edit cannot be found.'),
    (22, 400, 'Invalid page: Pages start at 1 and max at 500. They are expected to be an integer.'),
    (23, 400, 'Invalid date: Format needs to be YYYY-MM-DD.'),
    (24, 504, 'Your request to the backend server timed out. Try again.'),
    (25, 429, 'Your request count (#) is over the allowed limit of (40).'),
    (26, 400, 'You must provide a username and password.'),
    (27, 400, 'Too many append to response objects: The maximum number of remote calls is 20.'),
    (28, 400, 'Invalid timezone: Please consult the documentation for a valid timezone.'),
    (29, 400, 'You must confirm this action: Please provide a confirm=true parameter.'),
    (30, 401, 'Invalid username and/or password: You did not provide a valid login.'),
    (31, 401, 'Account disabled: Your account is no longer active. Contact TMDB if this is an error.'),
    (32, 401, 'Email not verified: Your email address has not been verified.'),
    (33, 401, 'Invalid request token: The request token is either expired or invalid.'),
    (34, 404, 'The resource you requested could not be found.'),
    (35, 401, 'Invalid token.'),
    (36, 401, "This token hasn't been granted write permission by the user."),
    (37, 404, 'The requested session could not be found.'),
    (38, 401, "You don't have permission to edit this resource."),
    (39, 401, 'This resource is private.'),
    (40, 200, 'Nothing to update.'),
    (41, 422, "This request token hasn't been approved by the user."),
    (42, 405, 'This request method is not supported for this resource.'),
    (43, 502, "Couldn't connect to the backend server."),
    (44, 500, 'The ID is invalid.'),
    (45, 403, 'This user has been suspended.'),
    (46, 503, 'The API is undergoing maintenance. Try again later.'),
    (47, 400, 'The input is not valid.'),
]

class ServiceDeprecationWarning(DeprecationWarning):
    """Service deprecation warning.

    Use this waring when the Service(protocol) is deprecate by TMDB.
    By default, python will not show deprecation warnings.

    """
    pass


class TmdbApiException(Exception):
    """TMDB API exception.

    An exception handle the response of the TMDB API.

    """
    pass


def type_checking(keyword, value):
    if keyword == "media_type":
        if value not in ("tv", "movie"):
            raise ValueError("Media Type should be 'tv' or 'movie'.")
        
    else:
        return False
    return True
