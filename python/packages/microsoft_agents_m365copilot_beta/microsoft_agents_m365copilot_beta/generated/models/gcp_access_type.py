from enum import Enum

class GcpAccessType(str, Enum):
    Public = "public",
    SubjectToObjectAcls = "subjectToObjectAcls",
    Private = "private",
    UnknownFutureValue = "unknownFutureValue",

