from enum import Enum

class DeviceManagementConfigurationDeviceMode(str, Enum):
    # No Device Mode specified
    None_ = "none",
    # Device must be in kiosk mode for this setting to apply
    Kiosk = "kiosk",

