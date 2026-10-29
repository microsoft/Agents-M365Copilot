from enum import Enum

class WindowsSModeConfiguration(str, Enum):
    # This option will remove all restrictions to unlock S mode - default
    NoRestriction = "noRestriction",
    # This option will block the user to unlock the device from S mode
    Block = "block",
    # This option will unlock the device from S mode
    Unlock = "unlock",

