from enum import Enum

class DeviceManagementConfigurationSettingRiskLevel(str, Enum):
    # Default. Low Risk Setting
    Low = "low",
    # Medium Risk Setting
    Medium = "medium",
    # High Risk Setting
    High = "high",

