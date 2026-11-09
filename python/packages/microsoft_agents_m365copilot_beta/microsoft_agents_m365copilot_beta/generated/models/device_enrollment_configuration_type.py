from enum import Enum

class DeviceEnrollmentConfigurationType(str, Enum):
    # Default. Set to unknown if the configuration type cannot be determined.
    Unknown = "unknown",
    # Indicates that configuration is of type limit which refers to number of devices a user is allowed to enroll.
    Limit = "limit",
    # Indicates that configuration is of type platform restriction which refers to types of devices a user is allowed to enroll.
    PlatformRestrictions = "platformRestrictions",
    # Indicates that configuration is of type Windows Hello which refers to authentication method devices would use.
    WindowsHelloForBusiness = "windowsHelloForBusiness",
    # Indicates that configuration is of type default limit which refers to types of devices a user is allowed to enroll by default.
    DefaultLimit = "defaultLimit",
    # Indicates that configuration is of type default platform restriction which refers to types of devices a user is allowed to enroll by default.
    DefaultPlatformRestrictions = "defaultPlatformRestrictions",
    # Indicates that configuration is of type default Windows Hello which refers to authentication method devices would use by default.
    DefaultWindowsHelloForBusiness = "defaultWindowsHelloForBusiness",
    # Indicates that configuration is of type default Enrollment status page which refers to startup page displayed during OOBE in Autopilot devices by default.
    DefaultWindows10EnrollmentCompletionPageConfiguration = "defaultWindows10EnrollmentCompletionPageConfiguration",
    # Indicates that configuration is of type Enrollment status page which refers to startup page displayed during OOBE in Autopilot devices.
    Windows10EnrollmentCompletionPageConfiguration = "windows10EnrollmentCompletionPageConfiguration",
    # Indicates that configuration is of type Comanagement Authority which refers to policies applied to Co-Managed devices.
    DeviceComanagementAuthorityConfiguration = "deviceComanagementAuthorityConfiguration",
    # Indicates that configuration is of type single platform restriction which refers to types of devices a user is allowed to enroll.
    SinglePlatformRestriction = "singlePlatformRestriction",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",
    # Indicates that configuration is of type Enrollment Notification which refers to types of notification a user receives during enrollment.
    EnrollmentNotificationsConfiguration = "enrollmentNotificationsConfiguration",
    # Indicates the configuration is of type Windows Restore which refers to the tenant level Windows Backup and Restore settings a user receives during out-of-box experience (OOBE) Windows enrollment
    WindowsRestore = "windowsRestore",

