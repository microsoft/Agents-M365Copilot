from enum import Enum

class KioskModeType(str, Enum):
    # Not configured
    NotConfigured = "notConfigured",
    # Run in single-app mode
    SingleAppMode = "singleAppMode",
    # Run in multi-app mode
    MultiAppMode = "multiAppMode",

