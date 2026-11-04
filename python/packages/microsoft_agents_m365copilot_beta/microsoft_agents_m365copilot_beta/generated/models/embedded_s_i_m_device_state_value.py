from enum import Enum

class EmbeddedSIMDeviceStateValue(str, Enum):
    # Designates that the embedded SIM activation code is free and available to be assigned to a device.
    NotEvaluated = "notEvaluated",
    # Designates that Intune Service failed to deliver this profile to a device.
    Failed = "failed",
    # Designates that the embedded SIM activation code has been assigned to a device and the device is installing the token.
    Installing = "installing",
    # Designates that the embedded SIM activation code has been successfully installed on the target device.
    Installed = "installed",
    # Designates that Intune Service is trying to delete the profile from the device.
    Deleting = "deleting",
    # Designates that there is error with this profile.
    Error = "error",
    # Designates that the profile is deleted from the device.
    Deleted = "deleted",
    # Designates that the profile is removed from the device by the user
    RemovedByUser = "removedByUser",

