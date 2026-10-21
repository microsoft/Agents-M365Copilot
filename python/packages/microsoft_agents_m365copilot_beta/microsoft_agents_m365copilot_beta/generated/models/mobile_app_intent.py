from enum import Enum

class MobileAppIntent(str, Enum):
    # Available
    Available = "available",
    # Not Available
    NotAvailable = "notAvailable",
    # Required Install
    RequiredInstall = "requiredInstall",
    # Required Uninstall
    RequiredUninstall = "requiredUninstall",
    # RequiredAndAvailableInstall
    RequiredAndAvailableInstall = "requiredAndAvailableInstall",
    # AvailableInstallWithoutEnrollment
    AvailableInstallWithoutEnrollment = "availableInstallWithoutEnrollment",
    # Exclude
    Exclude = "exclude",

