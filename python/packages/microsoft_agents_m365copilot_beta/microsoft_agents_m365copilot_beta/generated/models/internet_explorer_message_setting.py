from enum import Enum

class InternetExplorerMessageSetting(str, Enum):
    # Not configured.
    NotConfigured = "notConfigured",
    # Disabled.
    Disabled = "disabled",
    # Enabled.
    Enabled = "enabled",
    # KeepGoing.
    KeepGoing = "keepGoing",

