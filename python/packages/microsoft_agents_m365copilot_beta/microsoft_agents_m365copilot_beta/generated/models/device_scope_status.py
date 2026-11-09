from enum import Enum

class DeviceScopeStatus(str, Enum):
    # Indicates the device scope is not enabled and there are no calculations in progress.
    None_ = "none",
    # Indicates the device scope is enabled and report metrics data are being recalculated by the service.
    Computing = "computing",
    # Indicates the device scope is enabled but there is insufficient data to calculate results. The system requires information from at least 5 devices before calculations can occur.
    InsufficientData = "insufficientData",
    # Device scope is enabled and finished recalculating the report metric. Device scope is now ready to be used.
    Completed = "completed",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

