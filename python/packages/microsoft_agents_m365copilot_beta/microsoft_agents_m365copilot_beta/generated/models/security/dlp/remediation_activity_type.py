from enum import Enum

class RemediationActivityType(str, Enum):
    Unknown = "unknown",
    TemplateTriggered = "templateTriggered",
    IwUnableToTakeAction = "iwUnableToTakeAction",
    UnknownFutureValue = "unknownFutureValue",

