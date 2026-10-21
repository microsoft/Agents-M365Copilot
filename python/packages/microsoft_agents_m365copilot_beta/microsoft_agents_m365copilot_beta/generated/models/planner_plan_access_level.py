from enum import Enum

class PlannerPlanAccessLevel(str, Enum):
    ReadAccess = "readAccess",
    ReadWriteAccess = "readWriteAccess",
    FullAccess = "fullAccess",
    UnknownFutureValue = "unknownFutureValue",

