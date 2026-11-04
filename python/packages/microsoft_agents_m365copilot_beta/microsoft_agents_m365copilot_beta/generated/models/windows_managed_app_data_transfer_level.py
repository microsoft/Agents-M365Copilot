from enum import Enum

class WindowsManagedAppDataTransferLevel(str, Enum):
    # All apps.
    AllApps = "allApps",
    # No apps.
    None_ = "none",
    # Selected apps only. Allowed locations are specified by the child property.
    SelectedApps = "selectedApps",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

