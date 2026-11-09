from enum import Enum

class WindowsManagedAppDataTransferLocations(str, Enum):
    # No locations selected.
    None_ = "none",
    # OneDrive for Business. Data transferred to or from this location is subject to app protection policy.
    OneDriveForBusiness = "oneDriveForBusiness",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

