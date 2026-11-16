from enum import Enum

class DeviceActionCategory(str, Enum):
    # Action is performed on a single device alone
    Single = "single",
    # Action is performed for a set of devices
    Bulk = "bulk",

