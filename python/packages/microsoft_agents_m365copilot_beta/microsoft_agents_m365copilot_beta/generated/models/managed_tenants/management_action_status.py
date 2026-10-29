from enum import Enum

class ManagementActionStatus(str, Enum):
    ToAddress = "toAddress",
    Completed = "completed",
    Error = "error",
    TimeOut = "timeOut",
    InProgress = "inProgress",
    Planned = "planned",
    ResolvedBy3rdParty = "resolvedBy3rdParty",
    ResolvedThroughAlternateMitigation = "resolvedThroughAlternateMitigation",
    RiskAccepted = "riskAccepted",
    UnknownFutureValue = "unknownFutureValue",

