from enum import Enum

class AccessType(str, Enum):
    QuickAccess = "quickAccess",
    PrivateAccess = "privateAccess",
    UnknownFutureValue = "unknownFutureValue",
    AppAccess = "appAccess",

