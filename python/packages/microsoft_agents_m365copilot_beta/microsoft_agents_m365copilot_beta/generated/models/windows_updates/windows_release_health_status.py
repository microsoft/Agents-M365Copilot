from enum import Enum

class WindowsReleaseHealthStatus(str, Enum):
    Resolved = "resolved",
    MitigatedExternal = "mitigatedExternal",
    Mitigated = "mitigated",
    ResolvedExternal = "resolvedExternal",
    Confirmed = "confirmed",
    Reported = "reported",
    Investigating = "investigating",
    UnknownFutureValue = "unknownFutureValue",

