from enum import Enum

class SectionType(str, Enum):
    UserDefined = "userDefined",
    SystemDefined = "systemDefined",
    UnknownFutureValue = "unknownFutureValue",

