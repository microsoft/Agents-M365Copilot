from enum import Enum

class AdditionalUserAttributes(str, Enum):
    UserGradeLevel = "userGradeLevel",
    UserNumber = "userNumber",
    UnknownFutureValue = "unknownFutureValue",

