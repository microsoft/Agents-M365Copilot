from enum import Enum

class DeviceManagementConfigurationSettingAccessTypes(str, Enum):
    None_ = "none",
    Add = "add",
    Copy = "copy",
    Delete = "delete",
    Get = "get",
    Replace = "replace",
    Execute = "execute",

