from enum import Enum

class ManagedInstallerStatus(str, Enum):
    # Managed Installer is Disabled
    Disabled = "disabled",
    # Managed Installer is Enabled
    Enabled = "enabled",

