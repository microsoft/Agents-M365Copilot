from enum import Enum

class ServiceType(str, Enum):
    Unknown = "unknown",
    SharePoint = "sharePoint",
    Exchange = "exchange",
    OneDriveForBusiness = "oneDriveForBusiness",
    UnknownFutureValue = "unknownFutureValue",

