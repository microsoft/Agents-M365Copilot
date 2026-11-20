from enum import Enum

class MonitoringSignal(str, Enum):
    Rollback = "rollback",
    Ineligible = "ineligible",
    UnknownFutureValue = "unknownFutureValue",

