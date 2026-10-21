from enum import Enum

class BrowserSyncSetting(str, Enum):
    # Default – Allow syncing of browser settings across devices.
    NotConfigured = "notConfigured",
    # Prevent syncing of browser settings across user devices, allow user override of setting.
    BlockedWithUserOverride = "blockedWithUserOverride",
    # Absolutely prevent syncing of browser settings across user devices.
    Blocked = "blocked",

