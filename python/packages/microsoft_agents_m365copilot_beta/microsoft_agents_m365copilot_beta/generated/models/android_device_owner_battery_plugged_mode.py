from enum import Enum

class AndroidDeviceOwnerBatteryPluggedMode(str, Enum):
    # Not configured; this value is ignored.
    NotConfigured = "notConfigured",
    # Power source is an AC charger.
    Ac = "ac",
    # Power source is a USB port.
    Usb = "usb",
    # Power source is wireless.
    Wireless = "wireless",

