from enum import Enum

class OperatorType(str, Enum):
    GreaterOrEqual = "greaterOrEqual",
    Equal = "equal",
    Greater = "greater",
    Less = "less",
    LessOrEqual = "lessOrEqual",
    NotEqual = "notEqual",
    UnknownFutureValue = "unknownFutureValue",

