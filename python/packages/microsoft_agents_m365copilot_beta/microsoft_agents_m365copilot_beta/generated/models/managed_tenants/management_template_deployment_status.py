from enum import Enum

class ManagementTemplateDeploymentStatus(str, Enum):
    Unknown = "unknown",
    InProgress = "inProgress",
    Completed = "completed",
    Failed = "failed",
    Ineligible = "ineligible",
    UnknownFutureValue = "unknownFutureValue",

