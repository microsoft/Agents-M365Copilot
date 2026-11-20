from enum import Enum

class AndroidDeviceOwnerKioskModeScreenOrientation(str, Enum):
    # Not configured; this value is ignored.
    NotConfigured = "notConfigured",
    # Portrait orientation.
    Portrait = "portrait",
    # Landscape orientation.
    Landscape = "landscape",
    # Auto rotate between portrait and landscape orientations.
    AutoRotate = "autoRotate",

