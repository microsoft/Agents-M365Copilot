from enum import Enum

class CloudPcManagedLicenseType(str, Enum):
    Frontline = "frontline",
    Reserve = "reserve",
    UnknownFutureValue = "unknownFutureValue",

