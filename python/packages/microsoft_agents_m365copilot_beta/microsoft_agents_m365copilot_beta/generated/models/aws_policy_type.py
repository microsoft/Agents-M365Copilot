from enum import Enum

class AwsPolicyType(str, Enum):
    System = "system",
    Custom = "custom",
    UnknownFutureValue = "unknownFutureValue",

