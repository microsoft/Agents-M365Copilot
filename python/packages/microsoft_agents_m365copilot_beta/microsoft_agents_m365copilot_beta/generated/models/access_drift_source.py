from enum import Enum

class AccessDriftSource(str, Enum):
    Entra = "entra",
    ExternalApplication = "externalApplication",
    UnknownFutureValue = "unknownFutureValue",

