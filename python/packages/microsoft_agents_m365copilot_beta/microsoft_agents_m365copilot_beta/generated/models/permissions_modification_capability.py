from enum import Enum

class PermissionsModificationCapability(str, Enum):
    Enabled = "enabled",
    NotConfigured = "notConfigured",
    NoRecentDataCollected = "noRecentDataCollected",
    UnknownFutureValue = "unknownFutureValue",

