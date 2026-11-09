from enum import Enum

class ContinuousAccessEvaluationMode(str, Enum):
    StrictEnforcement = "strictEnforcement",
    Disabled = "disabled",
    UnknownFutureValue = "unknownFutureValue",
    StrictLocation = "strictLocation",

