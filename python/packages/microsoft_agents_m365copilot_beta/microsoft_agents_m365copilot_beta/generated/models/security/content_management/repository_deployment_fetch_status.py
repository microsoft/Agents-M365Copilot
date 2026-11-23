from enum import Enum

class RepositoryDeploymentFetchStatus(str, Enum):
    # Status fetched successfully.
    Success = "success",
    # Caller was not authorized to fetch status.
    Unauthorized = "unauthorized",
    # No deployment was found.
    NotFound = "notFound",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",
    # Provider status could not be fetched.
    Unavailable = "unavailable",

