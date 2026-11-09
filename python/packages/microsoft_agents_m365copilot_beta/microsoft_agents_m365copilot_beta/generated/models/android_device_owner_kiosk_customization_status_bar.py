from enum import Enum

class AndroidDeviceOwnerKioskCustomizationStatusBar(str, Enum):
    # Not configured; this value defaults to STATUS_BAR_UNSPECIFIED.
    NotConfigured = "notConfigured",
    # System info and notifications are shown on the status bar in kiosk mode.
    NotificationsAndSystemInfoEnabled = "notificationsAndSystemInfoEnabled",
    # Only system info is shown on the status bar in kiosk mode.
    SystemInfoOnly = "systemInfoOnly",

