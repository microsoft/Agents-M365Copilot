from enum import Enum

class WindowsQualityUpdatePolicyApprovalMethodType(str, Enum):
    # The updates need manually approve.
    Manual = "manual",
    # The updates would be automaticaly approved.
    Automatic = "automatic",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

