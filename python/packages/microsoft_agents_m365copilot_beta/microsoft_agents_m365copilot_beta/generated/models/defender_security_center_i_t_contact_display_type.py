from enum import Enum

class DefenderSecurityCenterITContactDisplayType(str, Enum):
    # Not Configured
    NotConfigured = "notConfigured",
    # Display in app and in notifications
    DisplayInAppAndInNotifications = "displayInAppAndInNotifications",
    # Display only in app
    DisplayOnlyInApp = "displayOnlyInApp",
    # Display only in notifications
    DisplayOnlyInNotifications = "displayOnlyInNotifications",

