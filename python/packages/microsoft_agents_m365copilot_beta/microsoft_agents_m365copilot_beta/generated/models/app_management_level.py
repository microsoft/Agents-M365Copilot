from enum import Enum

class AppManagementLevel(str, Enum):
    # Unspecified
    Unspecified = "unspecified",
    # Unmanaged
    Unmanaged = "unmanaged",
    # MDM
    Mdm = "mdm",
    # Android Enterprise
    AndroidEnterprise = "androidEnterprise",
    # Android Enterprise dedicated devices with Azure AD Shared mode
    AndroidEnterpriseDedicatedDevicesWithAzureAdSharedMode = "androidEnterpriseDedicatedDevicesWithAzureAdSharedMode",
    # Android Open Source Project (AOSP) devices
    AndroidOpenSourceProjectUserAssociated = "androidOpenSourceProjectUserAssociated",
    # Android Open Source Project (AOSP) userless devices
    AndroidOpenSourceProjectUserless = "androidOpenSourceProjectUserless",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

