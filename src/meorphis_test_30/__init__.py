# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from . import types
from ._types import NOT_GIVEN, NoneType, NotGiven, Transport, ProxiesTypes
from ._utils import file_from_path
from ._client import (
    ENVIRONMENTS,
    Client,
    Stream,
    Timeout,
    Transport,
    AsyncClient,
    AsyncStream,
    MeorphisTest30,
    RequestOptions,
    AsyncMeorphisTest30,
)
from ._models import BaseModel
from ._version import __title__, __version__
from ._response import APIResponse as APIResponse, AsyncAPIResponse as AsyncAPIResponse
from ._constants import DEFAULT_TIMEOUT, DEFAULT_MAX_RETRIES, DEFAULT_CONNECTION_LIMITS
from ._exceptions import (
    APIError,
    ConflictError,
    NotFoundError,
    APIStatusError,
    RateLimitError,
    APITimeoutError,
    BadRequestError,
    APIConnectionError,
    AuthenticationError,
    InternalServerError,
    MeorphisTest30Error,
    PermissionDeniedError,
    UnprocessableEntityError,
    APIResponseValidationError,
)
from ._utils._logs import setup_logging as _setup_logging

__all__ = [
    "types",
    "__version__",
    "__title__",
    "NoneType",
    "Transport",
    "ProxiesTypes",
    "NotGiven",
    "NOT_GIVEN",
    "MeorphisTest30Error",
    "APIError",
    "APIStatusError",
    "APITimeoutError",
    "APIConnectionError",
    "APIResponseValidationError",
    "BadRequestError",
    "AuthenticationError",
    "PermissionDeniedError",
    "NotFoundError",
    "ConflictError",
    "UnprocessableEntityError",
    "RateLimitError",
    "InternalServerError",
    "Timeout",
    "RequestOptions",
    "Client",
    "AsyncClient",
    "Stream",
    "AsyncStream",
    "MeorphisTest30",
    "AsyncMeorphisTest30",
    "ENVIRONMENTS",
    "file_from_path",
    "BaseModel",
    "DEFAULT_TIMEOUT",
    "DEFAULT_MAX_RETRIES",
    "DEFAULT_CONNECTION_LIMITS",
]

_setup_logging()

# Update the __module__ attribute for exported symbols so that
# error messages point to this module instead of the module
# it was originally defined in, e.g.
# meorphis_test_30._exceptions.NotFoundError -> meorphis_test_30.NotFoundError
__locals = locals()
for __name in __all__:
    if not __name.startswith("__"):
        try:
            __locals[__name].__module__ = "meorphis_test_30"
        except (TypeError, AttributeError):
            # Some of our exported symbols are builtins which we can't set attributes for.
            pass
