from enum import Enum

class ManagedDeviceManagementFeatures(str, Enum):
    # Unknown device management features.
    None_ = "none",
    # Microsoft Managed Desktop
    MicrosoftManagedDesktop = "microsoftManagedDesktop",

