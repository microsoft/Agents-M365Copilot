from enum import Enum

class WindowsKioskAppType(str, Enum):
    # Unknown.
    Unknown = "unknown",
    # Store App.
    Store = "store",
    # Desktop App.
    Desktop = "desktop",
    # Input by AUMID.
    AumId = "aumId",

