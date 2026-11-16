from enum import Enum

class ChassisType(str, Enum):
    # Unknown.
    Unknown = "unknown",
    # Desktop.
    Desktop = "desktop",
    # Laptop.
    Laptop = "laptop",
    # Workstation.
    WorksWorkstation = "worksWorkstation",
    # Enterprise server.
    EnterpriseServer = "enterpriseServer",
    # Phone.
    Phone = "phone",
    # Mobile tablet.
    Tablet = "tablet",
    # Other mobile.
    MobileOther = "mobileOther",
    # Unknown mobile.
    MobileUnknown = "mobileUnknown",

