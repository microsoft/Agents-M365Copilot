from enum import Enum

class IdJagScopeMappingType(str, Enum):
    Direct = "direct",
    Mapped = "mapped",
    Passthrough = "passthrough",
    UnknownFutureValue = "unknownFutureValue",

