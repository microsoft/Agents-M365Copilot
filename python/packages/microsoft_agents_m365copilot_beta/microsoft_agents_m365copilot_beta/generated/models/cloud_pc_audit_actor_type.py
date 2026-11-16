from enum import Enum

class CloudPcAuditActorType(str, Enum):
    ItPro = "itPro",
    Application = "application",
    Partner = "partner",
    UnknownFutureValue = "unknownFutureValue",

