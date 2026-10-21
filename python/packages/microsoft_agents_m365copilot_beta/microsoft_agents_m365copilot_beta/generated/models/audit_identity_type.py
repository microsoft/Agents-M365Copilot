from enum import Enum

class AuditIdentityType(str, Enum):
    Agent = "agent",
    ServicePrincipal = "servicePrincipal",
    UnknownFutureValue = "unknownFutureValue",

