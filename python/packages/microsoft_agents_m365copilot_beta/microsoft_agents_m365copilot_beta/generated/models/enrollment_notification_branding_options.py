from enum import Enum

class EnrollmentNotificationBrandingOptions(str, Enum):
    # Indicates that the template has no branding.
    None_ = "none",
    # Indicates that the Company Logo is included in the notification.
    IncludeCompanyLogo = "includeCompanyLogo",
    # Indicates that the Company Name is included in the notification.
    IncludeCompanyName = "includeCompanyName",
    # Indicates that the Contact Information is included in the notification.
    IncludeContactInformation = "includeContactInformation",
    # Indicates that the Company Portal Link is included in the notification.
    IncludeCompanyPortalLink = "includeCompanyPortalLink",
    # Indicates that the DeviceDetails is included in the notification.
    IncludeDeviceDetails = "includeDeviceDetails",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

