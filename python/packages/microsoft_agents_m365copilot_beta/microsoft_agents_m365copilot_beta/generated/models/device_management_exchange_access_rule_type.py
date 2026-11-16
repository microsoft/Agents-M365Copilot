from enum import Enum

class DeviceManagementExchangeAccessRuleType(str, Enum):
    # Family of devices
    Family = "family",
    # Specific model of device
    Model = "model",

