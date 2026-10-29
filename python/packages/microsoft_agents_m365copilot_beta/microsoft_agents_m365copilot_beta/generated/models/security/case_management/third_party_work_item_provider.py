from enum import Enum

class ThirdPartyWorkItemProvider(str, Enum):
    ServiceNow = "serviceNow",
    UnknownFutureValue = "unknownFutureValue",

