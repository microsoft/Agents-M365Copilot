from enum import Enum

class EdgeKioskModeRestrictionType(str, Enum):
    # Not configured (unrestricted).
    NotConfigured = "notConfigured",
    # Interactive/Digital signage in single-app mode.
    DigitalSignage = "digitalSignage",
    # Normal mode (full version of Microsoft Edge).
    NormalMode = "normalMode",
    # Public browsing in single-app mode.
    PublicBrowsingSingleApp = "publicBrowsingSingleApp",
    # Public browsing (inPrivate) in multi-app mode.
    PublicBrowsingMultiApp = "publicBrowsingMultiApp",

