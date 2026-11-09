from enum import Enum

class MicrosoftLauncherSearchBarPlacement(str, Enum):
    # Not configured; this value is ignored.
    NotConfigured = "notConfigured",
    # Indicates that the search bar will be displayed on the top of the device.
    Top = "top",
    # Indicates that the search bar will be displayed on the bottom of the device.
    Bottom = "bottom",
    # Indicates that the search bar will be hidden on the device.
    Hide = "hide",

