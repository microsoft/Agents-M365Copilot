from enum import Enum

class UserType(str, Enum):
    Regular = "regular",
    Admin = "admin",
    System = "system",
    UnknownFutureValue = "unknownFutureValue",

