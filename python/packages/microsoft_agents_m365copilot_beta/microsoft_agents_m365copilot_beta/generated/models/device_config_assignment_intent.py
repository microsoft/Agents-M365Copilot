from enum import Enum

class DeviceConfigAssignmentIntent(str, Enum):
    # Ensure that the configuration profile is applied to the devices in the assignment.
    Apply = "apply",
    # Ensure that the configuration profile is removed from devices that have previously installed the configuration profile.
    Remove = "remove",

