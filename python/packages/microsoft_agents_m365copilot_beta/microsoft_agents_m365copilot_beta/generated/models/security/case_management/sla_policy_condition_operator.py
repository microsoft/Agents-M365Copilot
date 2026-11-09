from enum import Enum

class SlaPolicyConditionOperator(str, Enum):
    Equals = "equals",
    NotEquals = "notEquals",
    Contains = "contains",
    DoesNotContain = "doesNotContain",
    IsEmpty = "isEmpty",
    IsNotEmpty = "isNotEmpty",
    Changed = "changed",
    ChangedTo = "changedTo",
    ChangedFrom = "changedFrom",
    IsBefore = "isBefore",
    IsAfter = "isAfter",
    GreaterThan = "greaterThan",
    LessThan = "lessThan",
    AnyOf = "anyOf",
    NoneOf = "noneOf",
    UnknownFutureValue = "unknownFutureValue",

