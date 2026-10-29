from enum import Enum

class PurviewInsiderRiskManagementLevel(str, Enum):
    None_ = "none",
    Minor = "minor",
    Moderate = "moderate",
    Elevated = "elevated",
    UnknownFutureValue = "unknownFutureValue",

