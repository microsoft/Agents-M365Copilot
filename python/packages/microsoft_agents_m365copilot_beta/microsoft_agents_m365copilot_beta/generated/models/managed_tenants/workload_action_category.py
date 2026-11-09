from enum import Enum

class WorkloadActionCategory(str, Enum):
    Automated = "automated",
    Manual = "manual",
    UnknownFutureValue = "unknownFutureValue",

