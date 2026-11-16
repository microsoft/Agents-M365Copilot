from enum import Enum

class DeviceAndAppManagementAssignmentFilterType(str, Enum):
    # Default value. Do not use.
    None_ = "none",
    # Indicates in-filter, rule matching will offer the payload to devices.
    Include = "include",
    # Indicates out-filter, rule matching will not offer the payload to devices.
    Exclude = "exclude",

