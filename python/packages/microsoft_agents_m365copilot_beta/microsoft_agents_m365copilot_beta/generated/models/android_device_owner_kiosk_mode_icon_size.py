from enum import Enum

class AndroidDeviceOwnerKioskModeIconSize(str, Enum):
    # Not configured; this value is ignored.
    NotConfigured = "notConfigured",
    # Smallest icon size.
    Smallest = "smallest",
    # Small icon size.
    Small = "small",
    # Regular icon size.
    Regular = "regular",
    # Large icon size.
    Large = "large",
    # Largest icon size.
    Largest = "largest",

