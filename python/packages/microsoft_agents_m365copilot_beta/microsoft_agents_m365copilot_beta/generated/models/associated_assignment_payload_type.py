from enum import Enum

class AssociatedAssignmentPayloadType(str, Enum):
    # Invalid payload type
    Unknown = "unknown",
    # Indicates that this filter is associated with a configuration or compliance policy payload type
    DeviceConfigurationAndCompliance = "deviceConfigurationAndCompliance",
    # Indicates that this assignment filter is associated with an application payload type
    Application = "application",
    # Indicates that this filter is associated with a Android Enterprise application payload type
    AndroidEnterpriseApp = "androidEnterpriseApp",
    # Indicates that this filter is associated with an enrollment restriction or enrollment status page policy payload type
    EnrollmentConfiguration = "enrollmentConfiguration",
    # Indicates that this filter is associated with an Administrative Template policy payload type
    GroupPolicyConfiguration = "groupPolicyConfiguration",
    # Indicates that this assignment filter is associated with Zero touch deployment Device Configuration Profile payload type
    ZeroTouchDeploymentDeviceConfigProfile = "zeroTouchDeploymentDeviceConfigProfile",
    # Indicates that this filter is associated with an Android Enterprise Configuration policy payload type
    AndroidEnterpriseConfiguration = "androidEnterpriseConfiguration",
    # Indicates that this assignment filter is associated with Device Firmware Configuration Interface(DCFI) payload type
    DeviceFirmwareConfigurationInterfacePolicy = "deviceFirmwareConfigurationInterfacePolicy",
    # Indicates that this filter is associated with a resource access policy (Wifi, VPN, Certificate) payload type
    ResourceAccessPolicy = "resourceAccessPolicy",
    # Indicates that this filter is associated with a Win32 app payload type
    Win32app = "win32app",
    # Indicates that this filter is associated with a configuration or compliance policy on Device Configuration v2 Infrastructure payload type
    DeviceManagmentConfigurationAndCompliancePolicy = "deviceManagmentConfigurationAndCompliancePolicy",

