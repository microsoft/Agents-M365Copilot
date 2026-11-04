from enum import Enum

class MeteredConnectionLimitType(str, Enum):
    # Unrestricted
    Unrestricted = "unrestricted",
    # Fixed
    Fixed = "fixed",
    # Variable
    Variable = "variable",

