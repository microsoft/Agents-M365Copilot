from enum import Enum

class DeviceAssignmentItemStatus(str, Enum):
    # Default. Indicates that the device assignment action to remove or restore an application or a configuration is 'initiated' on the managed device
    Initiated = "initiated",
    # Indicates that the device assignment action to remove or restore an application or a configuration is 'in progress' on the managed device
    InProgress = "inProgress",
    # Indicates that the application or configuration has been successfully removed on the managed device
    Removed = "removed",
    # Indicates that the application or configuration has failed to be removed or restored on the managed device. The error may be retriable depending on the intent action message and error code
    Error = "error",
    # Indicates that the application or configuration has been successfully restored on the managed device
    Succeeded = "succeeded",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

