from enum import Enum

class WindowsAutoUpdateCatalogAppNotificationType(str, Enum):
    # Indicates that all notifications related to app installation and restart are displayed to the end user.
    ShowAll = "showAll",
    # Indicates that only restart notifications are displayed to the end user; other installation progress notifications are suppressed.
    ShowReboot = "showReboot",
    # Indicates that all notifications related to app installation and restart are suppressed. The end user is not informed of the installation or pending restarts.
    HideAll = "hideAll",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

