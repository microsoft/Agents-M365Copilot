from enum import Enum

class MicrosoftLauncherDockPresence(str, Enum):
    # Not configured; this value is ignored.
    NotConfigured = "notConfigured",
    # Indicates the device's dock will be displayed on the device.
    Show = "show",
    # Indicates the device's dock will be hidden on the device, but the user can access the dock by dragging the handler on the bottom of the screen.
    Hide = "hide",
    # Indicates the device's dock will be disabled on the device.
    Disabled = "disabled",

