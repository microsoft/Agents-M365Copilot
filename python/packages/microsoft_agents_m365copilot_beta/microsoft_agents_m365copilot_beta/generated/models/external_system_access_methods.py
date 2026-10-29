from enum import Enum

class ExternalSystemAccessMethods(str, Enum):
    Direct = "direct",
    RoleChaining = "roleChaining",
    UnknownFutureValue = "unknownFutureValue",

