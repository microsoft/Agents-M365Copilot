from enum import Enum

class SlaPolicyLogicalOperator(str, Enum):
    And_ = "and",
    Or_ = "or",
    UnknownFutureValue = "unknownFutureValue",

