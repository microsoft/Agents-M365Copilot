from enum import Enum

class DeviceManagementConfigurationSettingVisibility(str, Enum):
    # Default. Not visible.
    None_ = "none",
    # Visible to setting catalog policy type.
    SettingsCatalog = "settingsCatalog",
    # Visible to template policy type.
    Template = "template",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

