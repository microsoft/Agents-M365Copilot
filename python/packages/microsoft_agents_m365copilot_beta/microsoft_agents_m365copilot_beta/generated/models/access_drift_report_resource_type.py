from enum import Enum

class AccessDriftReportResourceType(str, Enum):
    Application = "application",
    Group = "group",
    UnknownFutureValue = "unknownFutureValue",

