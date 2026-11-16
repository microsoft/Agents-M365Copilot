from enum import Enum

class ChangeUefiSettingsPermission(str, Enum):
    # Device default value, no intent.
    NotConfiguredOnly = "notConfiguredOnly",
    # Prevent change of UEFI setting permission
    None_ = "none",

