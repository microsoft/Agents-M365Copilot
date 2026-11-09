from enum import Enum

class AllowedRolePrincipalTypes(str, Enum):
    User = "user",
    ServicePrincipal = "servicePrincipal",
    Group = "group",
    UnknownFutureValue = "unknownFutureValue",

