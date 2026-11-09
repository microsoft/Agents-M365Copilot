from enum import Enum

class WindowsQualityUpdateCategory(str, Enum):
    # All update type
    All = "all",
    # Security only update type
    Security = "security",
    # Non security only update type
    NonSecurity = "nonSecurity",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",
    # Quick machine recovery update type
    QuickMachineRecovery = "quickMachineRecovery",

