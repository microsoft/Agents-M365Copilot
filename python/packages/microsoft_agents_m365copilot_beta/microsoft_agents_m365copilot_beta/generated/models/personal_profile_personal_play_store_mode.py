from enum import Enum

class PersonalProfilePersonalPlayStoreMode(str, Enum):
    # Not configured.
    NotConfigured = "notConfigured",
    # Blocked Apps.
    BlockedApps = "blockedApps",
    # Allowed Apps.
    AllowedApps = "allowedApps",

