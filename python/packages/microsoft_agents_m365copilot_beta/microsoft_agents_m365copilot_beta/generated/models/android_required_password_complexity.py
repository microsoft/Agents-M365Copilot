from enum import Enum

class AndroidRequiredPasswordComplexity(str, Enum):
    # Device default value, no password.
    None_ = "none",
    # The required password complexity on the device is of type low as defined by the Android documentation.
    Low = "low",
    # The required password complexity on the device is of type medium as defined by the Android documentation.
    Medium = "medium",
    # The required password complexity on the device is of type high as defined by the Android documentation.
    High = "high",

