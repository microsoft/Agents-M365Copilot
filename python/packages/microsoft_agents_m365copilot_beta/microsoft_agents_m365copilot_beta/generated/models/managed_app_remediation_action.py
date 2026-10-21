from enum import Enum

class ManagedAppRemediationAction(str, Enum):
    # Indicates the user will be blocked from accessing the app and corporate data
    Block = "block",
    # Indicates the corporate data will be removed from the app
    Wipe = "wipe",
    # Indicates user will be warned the when accessing the app
    Warn = "warn",
    # Indicates user will be blocked from accessing the app and corporate data if devices supports this setting
    BlockWhenSettingIsSupported = "blockWhenSettingIsSupported",

