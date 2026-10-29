from enum import Enum

class DeviceAssignmentItemType(str, Enum):
    # Default. Indicates that the device assignment item type for the action is graph.mobileApp. Application is uninstalled on removal and installed back on restoration
    Application = "application",
    # Indicates that the device assignment item type for the action is graph.deviceConfiguration. DeviceConfiguration associated settings are removed on removal and added back on restoration
    DeviceConfiguration = "deviceConfiguration",
    # Indicates that the device assignment item type for the action is graph.deviceManagementConfigurationPolicy. DeviceManagementConfigurationPolicy associated settings are removed on removal and added back on restoration
    DeviceManagementConfigurationPolicy = "deviceManagementConfigurationPolicy",
    # Indicates that the device assignment item type for the action is `graph.managedDeviceMobileAppConfiguration`. MobileAppConfiguration associated settings are removed on removal and added back on restoration
    MobileAppConfiguration = "mobileAppConfiguration",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

