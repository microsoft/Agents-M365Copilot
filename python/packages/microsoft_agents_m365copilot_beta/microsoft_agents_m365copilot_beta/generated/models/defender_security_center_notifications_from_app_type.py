from enum import Enum

class DefenderSecurityCenterNotificationsFromAppType(str, Enum):
    # Not Configured
    NotConfigured = "notConfigured",
    # Block non-critical notifications
    BlockNoncriticalNotifications = "blockNoncriticalNotifications",
    # Block all notifications
    BlockAllNotifications = "blockAllNotifications",

