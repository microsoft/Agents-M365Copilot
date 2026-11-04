from enum import Enum

class LostModeState(str, Enum):
    # Lost mode is disabled.
    Disabled = "disabled",
    # Lost mode is enabled.
    Enabled = "enabled",

