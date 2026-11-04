from enum import Enum

class DeviceAndAppManagementAssignmentSource(str, Enum):
    # Direct indicates a direct assignment.
    Direct = "direct",
    # PolicySets indicates assignment was made via PolicySet assignment.
    PolicySets = "policySets",

