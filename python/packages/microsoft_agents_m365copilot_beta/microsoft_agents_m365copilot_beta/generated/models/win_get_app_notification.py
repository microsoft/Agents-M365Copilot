from enum import Enum

class WinGetAppNotification(str, Enum):
    # Show all notifications.
    ShowAll = "showAll",
    # Only show restart notification and suppress other notifications.
    ShowReboot = "showReboot",
    # Hide all notifications.
    HideAll = "hideAll",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

