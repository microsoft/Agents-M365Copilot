from enum import Enum

class CloudPcDisasterRecoveryType(str, Enum):
    NotConfigured = "notConfigured",
    CrossRegion = "crossRegion",
    Premium = "premium",
    UnknownFutureValue = "unknownFutureValue",

