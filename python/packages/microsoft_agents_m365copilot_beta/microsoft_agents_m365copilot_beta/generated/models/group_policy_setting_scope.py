from enum import Enum

class GroupPolicySettingScope(str, Enum):
    # Device scope unknown
    Unknown = "unknown",
    # Device scope
    Device = "device",
    # User scope
    User = "user",

