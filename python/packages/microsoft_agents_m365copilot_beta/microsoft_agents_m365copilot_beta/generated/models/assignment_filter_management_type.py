from enum import Enum

class AssignmentFilterManagementType(str, Enum):
    # Indicates when filter is supported based on device properties. This is the default value when management type resolution fails.
    Devices = "devices",
    # Indicates when filter is supported based on app properties.
    Apps = "apps",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

