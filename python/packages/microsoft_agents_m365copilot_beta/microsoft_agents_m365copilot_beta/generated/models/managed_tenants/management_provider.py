from enum import Enum

class ManagementProvider(str, Enum):
    Microsoft = "microsoft",
    Community = "community",
    IndirectProvider = "indirectProvider",
    Self = "self",
    UnknownFutureValue = "unknownFutureValue",

