from enum import Enum

class Category(str, Enum):
    Unknown = "unknown",
    Authentication = "authentication",
    UnknownFutureValue = "unknownFutureValue",

