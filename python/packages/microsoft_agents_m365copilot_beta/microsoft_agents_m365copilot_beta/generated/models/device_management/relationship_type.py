from enum import Enum

class RelationshipType(str, Enum):
    And_ = "and",
    Or_ = "or",
    UnknownFutureValue = "unknownFutureValue",

