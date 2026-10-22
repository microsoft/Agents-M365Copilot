from enum import Enum

class MacOSPriority(str, Enum):
    # Indicates low scheduling priority for downloading and preparing the requested update
    Low = "low",
    # Indicates high scheduling priority for downloading and preparing the requested update
    High = "high",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

