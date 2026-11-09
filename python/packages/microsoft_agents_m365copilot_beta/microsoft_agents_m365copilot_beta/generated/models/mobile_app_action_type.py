from enum import Enum

class MobileAppActionType(str, Enum):
    # Unknown result.
    Unknown = "unknown",
    # Application install command was sent.
    InstallCommandSent = "installCommandSent",
    # Application installed.
    Installed = "installed",
    # Application uninstalled.
    Uninstalled = "uninstalled",
    # User requested installation
    UserRequestedInstall = "userRequestedInstall",

