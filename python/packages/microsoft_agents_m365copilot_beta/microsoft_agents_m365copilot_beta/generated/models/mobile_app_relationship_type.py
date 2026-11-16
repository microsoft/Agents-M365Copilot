from enum import Enum

class MobileAppRelationshipType(str, Enum):
    # Indicates that the target of a relationship is the child in the relationship.
    Child = "child",
    # Indicates that the target of a relationship is the parent in the relationship.
    Parent = "parent",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

