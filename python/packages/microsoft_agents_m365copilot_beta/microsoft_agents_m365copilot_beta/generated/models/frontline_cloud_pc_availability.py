from enum import Enum

class FrontlineCloudPcAvailability(str, Enum):
    NotApplicable = "notApplicable",
    Available = "available",
    NotAvailable = "notAvailable",
    UnknownFutureValue = "unknownFutureValue",

