from enum import Enum

class InkAccessSetting(str, Enum):
    # Not configured.
    NotConfigured = "notConfigured",
    # Enabled.
    Enabled = "enabled",
    # Disabled.
    Disabled = "disabled",

