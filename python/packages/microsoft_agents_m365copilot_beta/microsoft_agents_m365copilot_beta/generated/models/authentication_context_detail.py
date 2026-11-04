from enum import Enum

class AuthenticationContextDetail(str, Enum):
    Required = "required",
    PreviouslySatisfied = "previouslySatisfied",
    NotApplicable = "notApplicable",
    UnknownFutureValue = "unknownFutureValue",

