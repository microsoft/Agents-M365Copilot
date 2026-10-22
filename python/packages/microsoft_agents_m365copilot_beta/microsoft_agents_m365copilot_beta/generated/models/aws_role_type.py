from enum import Enum

class AwsRoleType(str, Enum):
    System = "system",
    Custom = "custom",
    UnknownFutureValue = "unknownFutureValue",

