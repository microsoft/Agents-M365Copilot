from enum import Enum

class RoleAssignmentScopeType(str, Enum):
    # Default. Indicates that assignments are allowed to the specified resource scopes. Resource scopes are listed as Entra ID security group IDs.
    ResourceScope = "resourceScope",
    # Indicates that assignments are allowed to all Intune devices. Note that this does not map to any Entra ID security group, it is internal to Intune.
    AllDevices = "allDevices",
    # Indicates that assignments are allowed to all Intune licensed users. Note that this does not map to any Entra ID security group, it is internal to Intune.
    AllLicensedUsers = "allLicensedUsers",
    # Indicates that assignments are allowed to all Intune devices and licensed users. Note that this does not map to any Entra ID security group, it is internal to Intune.
    AllDevicesAndLicensedUsers = "allDevicesAndLicensedUsers",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

