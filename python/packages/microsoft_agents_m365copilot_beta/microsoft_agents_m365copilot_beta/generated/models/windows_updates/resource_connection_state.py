from enum import Enum

class ResourceConnectionState(str, Enum):
    Connected = "connected",
    NotAuthorized = "notAuthorized",
    NotFound = "notFound",
    UnknownFutureValue = "unknownFutureValue",

