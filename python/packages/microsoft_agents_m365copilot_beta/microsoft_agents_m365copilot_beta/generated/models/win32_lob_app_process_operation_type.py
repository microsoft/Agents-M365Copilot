from enum import Enum

class Win32LobAppProcessOperationType(str, Enum):
    # Default. Not configured.
    NotConfigured = "notConfigured",
    # Indicates that the rule evaluates whether the specified process exists (is running) on the device.
    Exists = "exists",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

