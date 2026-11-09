from enum import Enum

class LifecyclePolicyRelationship(str, Enum):
    Effective = "effective",
    InScopeButIneffective = "inScopeButIneffective",
    Pending = "pending",
    UnknownFutureValue = "unknownFutureValue",

