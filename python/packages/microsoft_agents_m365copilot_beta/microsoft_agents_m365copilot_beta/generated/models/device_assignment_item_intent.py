from enum import Enum

class DeviceAssignmentItemIntent(str, Enum):
    # Default. Indicates that the deployed application or configuration is intended to be removed on the managed device
    Remove = "remove",
    # Indicates that the application or configuration already under removal through previous actions and is now intended to be restored on the managed device
    Restore = "restore",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

