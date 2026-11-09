from enum import Enum

class SecurityRequirementState(str, Enum):
    Active = "active",
    Preview = "preview",
    UnknownFutureValue = "unknownFutureValue",

