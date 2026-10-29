from enum import Enum

class OperationApprovalPolicyType(str, Enum):
    # Default. Indicates that the configured policy type is unknown. Not a valid policy type in an OperationApprovalPolicy.
    Unknown = "unknown",
    # Indicates that the configured policy type is for a Device Wipe Action.
    DeviceWipe = "deviceWipe",
    # Indicates that the configured policy type is for a Device Retire Action
    DeviceRetire = "deviceRetire",
    # Indicates that the configured policy type is for a Device Delete Action.
    DeviceDelete = "deviceDelete",
    # Indicates that the configured policy type is an application type, such as mobile apps or built-in apps.
    App = "app",
    # Indicates that the configured policy type is a script type, such as PowerShell scripts or remediation scripts.
    Script = "script",
    # Indicates that the configured policy type type is for Intune roles, such as application administrator or a custom role.
    Role = "role",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",
    # Indicates that the configured policy type is for Tenant Configuration operations.
    TenantConfiguration = "tenantConfiguration",
    # Indicates that the configured policy type is for a Device Deprovision Action.
    DeviceDeprovision = "deviceDeprovision",

