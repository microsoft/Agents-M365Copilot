from enum import Enum

class AuthenticationAppPolicyStatus(str, Enum):
    Unknown = "unknown",
    AppLockOutOfDate = "appLockOutOfDate",
    AppLockEnabled = "appLockEnabled",
    AppLockDisabled = "appLockDisabled",
    AppContextOutOfDate = "appContextOutOfDate",
    AppContextShown = "appContextShown",
    AppContextNotShown = "appContextNotShown",
    LocationContextOutOfDate = "locationContextOutOfDate",
    LocationContextShown = "locationContextShown",
    LocationContextNotShown = "locationContextNotShown",
    NumberMatchOutOfDate = "numberMatchOutOfDate",
    NumberMatchCorrectNumberEntered = "numberMatchCorrectNumberEntered",
    NumberMatchIncorrectNumberEntered = "numberMatchIncorrectNumberEntered",
    NumberMatchDeny = "numberMatchDeny",
    TamperResistantHardwareOutOfDate = "tamperResistantHardwareOutOfDate",
    TamperResistantHardwareUsed = "tamperResistantHardwareUsed",
    TamperResistantHardwareNotUsed = "tamperResistantHardwareNotUsed",
    UnknownFutureValue = "unknownFutureValue",

