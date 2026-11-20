from enum import Enum

class PermissionKind(str, Enum):
    All = "all",
    Enumerated = "enumerated",
    AllPermissionsOnResourceApp = "allPermissionsOnResourceApp",
    UnknownFutureValue = "unknownFutureValue",

