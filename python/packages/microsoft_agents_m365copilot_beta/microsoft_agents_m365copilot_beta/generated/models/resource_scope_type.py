from enum import Enum

class ResourceScopeType(str, Enum):
    Group = "group",
    Chat = "chat",
    Tenant = "tenant",
    UnknownFutureValue = "unknownFutureValue",
    Team = "team",

