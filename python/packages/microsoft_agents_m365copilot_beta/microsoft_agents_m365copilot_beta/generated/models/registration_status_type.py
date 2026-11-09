from enum import Enum

class RegistrationStatusType(str, Enum):
    Registered = "registered",
    Enabled = "enabled",
    Capable = "capable",
    MfaRegistered = "mfaRegistered",
    UnknownFutureValue = "unknownFutureValue",

