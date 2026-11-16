from enum import Enum

class DeviceManagementAutopilotPolicyType(str, Enum):
    Unknown = "unknown",
    Application = "application",
    AppModel = "appModel",
    ConfigurationPolicy = "configurationPolicy",

