from enum import Enum

class DeviceManagementExchangeAccessLevel(str, Enum):
    # No device access rule has been configured in Exchange.
    None_ = "none",
    # Allow the device access to Exchange.
    Allow = "allow",
    # Block the device from accessing Exchange.
    Block = "block",
    # Quarantine the device in Exchange.
    Quarantine = "quarantine",

