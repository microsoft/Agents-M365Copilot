from enum import Enum

class EvaluationScopeType(str, Enum):
    Tenant = "tenant",
    Agent = "agent",
    AnonymousUser = "anonymousUser",
    UnknownFutureValue = "unknownFutureValue",

