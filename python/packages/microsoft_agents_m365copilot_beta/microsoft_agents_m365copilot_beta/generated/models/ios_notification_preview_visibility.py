from enum import Enum

class IosNotificationPreviewVisibility(str, Enum):
    # Notification preview settings will not be overwritten.
    NotConfigured = "notConfigured",
    # Always show notification previews.
    AlwaysShow = "alwaysShow",
    # Only show notification previews when the device is unlocked.
    HideWhenLocked = "hideWhenLocked",
    # Never show notification previews.
    NeverShow = "neverShow",

