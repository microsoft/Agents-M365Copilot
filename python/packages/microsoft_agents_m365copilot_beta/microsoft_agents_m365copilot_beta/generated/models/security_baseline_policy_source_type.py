from enum import Enum

class SecurityBaselinePolicySourceType(str, Enum):
    DeviceConfiguration = "deviceConfiguration",
    DeviceIntent = "deviceIntent",

