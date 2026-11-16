from enum import Enum

class DeviceManagementConfigurationAppleApplicabilityDeviceType(str, Enum):
    # No applicability
    None_ = "none",
    # Applies to iOS devices
    Ios = "ios",
    # Applies to Shared iPad devices.
    SharediPad = "sharediPad",
    # Applies to macOS devices
    MacOS = "macOS",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

