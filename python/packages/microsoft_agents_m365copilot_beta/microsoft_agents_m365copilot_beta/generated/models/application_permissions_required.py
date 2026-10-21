from enum import Enum

class ApplicationPermissionsRequired(str, Enum):
    Unknown = "unknown",
    Anonymous = "anonymous",
    Guest = "guest",
    User = "user",
    Administrator = "administrator",
    System = "system",
    UnknownFutureValue = "unknownFutureValue",

