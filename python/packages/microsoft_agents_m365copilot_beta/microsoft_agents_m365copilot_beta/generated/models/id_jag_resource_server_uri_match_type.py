from enum import Enum

class IdJagResourceServerUriMatchType(str, Enum):
    Absent = "absent",
    Exact = "exact",
    PathPrefix = "pathPrefix",
    AnyURI = "anyURI",
    UnknownFutureValue = "unknownFutureValue",

