from enum import Enum

class DeviceGuardVirtualizationBasedSecurityState(str, Enum):
    # Running
    Running = "running",
    # Root required
    RebootRequired = "rebootRequired",
    # 64 bit architecture required
    Require64BitArchitecture = "require64BitArchitecture",
    # Not licensed
    NotLicensed = "notLicensed",
    # Not configured
    NotConfigured = "notConfigured",
    # System does not meet hardware requirements
    DoesNotMeetHardwareRequirements = "doesNotMeetHardwareRequirements",
    # Other. Event logs in microsoft-Windows-DeviceGuard have more details.
    Other = "other",

