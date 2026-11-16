from enum import Enum

class DeviceHealthScriptType(str, Enum):
    # Indicates this is a device health script.
    DeviceHealthScript = "deviceHealthScript",
    # Indicates this is a managed installer script.
    ManagedInstallerScript = "managedInstallerScript",

