from enum import Enum

class MacOSSoftwareUpdateDelayPolicy(str, Enum):
    # Software update delays will not be enforced.
    None_ = "none",
    # Force delays for OS software updates.
    DelayOSUpdateVisibility = "delayOSUpdateVisibility",
    # Force delays for app software updates.
    DelayAppUpdateVisibility = "delayAppUpdateVisibility",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",
    # Force delays for major OS software updates.
    DelayMajorOsUpdateVisibility = "delayMajorOsUpdateVisibility",

