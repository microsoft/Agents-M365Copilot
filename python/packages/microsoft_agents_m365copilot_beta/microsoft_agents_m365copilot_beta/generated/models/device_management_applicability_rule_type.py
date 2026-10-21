from enum import Enum

class DeviceManagementApplicabilityRuleType(str, Enum):
    # Include
    Include = "include",
    # Exclude
    Exclude = "exclude",

