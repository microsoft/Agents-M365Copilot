from enum import Enum

class WindowsUpdateStatus(str, Enum):
    # There are no pending updates, no pending reboot updates and no failed updates.
    UpToDate = "upToDate",
    # There are updates that’s pending installation which includes updates that are not approved. There are no Pending reboot updates, no failed updates.
    PendingInstallation = "pendingInstallation",
    # There are updates that requires reboot. There are not failed updates.
    PendingReboot = "pendingReboot",
    # There are updates failed to install on the device.
    Failed = "failed",

