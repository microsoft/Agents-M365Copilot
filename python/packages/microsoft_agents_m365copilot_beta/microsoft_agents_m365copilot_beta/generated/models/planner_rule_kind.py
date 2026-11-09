from enum import Enum

class PlannerRuleKind(str, Enum):
    TaskRule = "taskRule",
    BucketRule = "bucketRule",
    PlanRule = "planRule",
    UnknownFutureValue = "unknownFutureValue",

