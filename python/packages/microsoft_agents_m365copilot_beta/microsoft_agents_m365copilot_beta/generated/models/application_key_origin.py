from enum import Enum

class ApplicationKeyOrigin(str, Enum):
    Application = "application",
    ServicePrincipal = "servicePrincipal",
    UnknownFutureValue = "unknownFutureValue",

