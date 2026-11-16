from enum import Enum

class WindowsPrivacyDataAccessLevel(str, Enum):
    # No access level specified, no intents. Device may behave either as in UserInControl or ForceAllow. It may depend on the privacy data been accessed, Windows versions and other factors.
    NotConfigured = "notConfigured",
    # Apps will be allowed to access the specified privacy data.
    ForceAllow = "forceAllow",
    # Apps will be denied to access specified privacy data.
    ForceDeny = "forceDeny",
    # Users will be prompted when apps try to access specified privacy data.
    UserInControl = "userInControl",

