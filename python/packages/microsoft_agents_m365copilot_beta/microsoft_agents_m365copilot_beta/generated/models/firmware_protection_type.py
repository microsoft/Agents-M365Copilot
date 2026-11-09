from enum import Enum

class FirmwareProtectionType(str, Enum):
    # Indicates that the device is not a Windows 11 device.
    NotApplicable = "notApplicable",
    # Indicates that System Guard Secure Launch is enabled for Firmware protection.
    SystemGuardSecureLaunch = "systemGuardSecureLaunch",
    # Indicates that Firmware Attack Surface Reduction is enabled for Firmware protection. This is only applicable to Surface devices.
    FirmwareAttackSurfaceReduction = "firmwareAttackSurfaceReduction",
    # Indicates that the device has Firmware protection disabled.
    Disabled = "disabled",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

