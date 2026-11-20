from enum import Enum

class VpnClientAuthenticationType(str, Enum):
    # User Authentication
    UserAuthentication = "userAuthentication",
    # Device Authentication
    DeviceAuthentication = "deviceAuthentication",

