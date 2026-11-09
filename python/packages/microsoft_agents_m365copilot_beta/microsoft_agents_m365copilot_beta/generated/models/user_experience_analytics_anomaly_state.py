from enum import Enum

class UserExperienceAnalyticsAnomalyState(str, Enum):
    # Indicates the state of anomaly is new.
    New = "new",
    # Indicates the state of anomaly is active.
    Active = "active",
    # Indicates the state of anomaly is disabled.
    Disabled = "disabled",
    # Indicates the state of anomaly is removed.
    Removed = "removed",
    # Indicates the state of anomaly is undefined.
    Other = "other",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

