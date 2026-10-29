from enum import Enum

class WritingToolsIosManagedAppConfigurationState(str, Enum):
    # Setting is not blocked
    NotBlocked = "notBlocked",
    # Setting is blocked
    Blocked = "blocked",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

