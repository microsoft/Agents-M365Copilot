from enum import Enum

class UserExperienceAnalyticsAnomalyCorrelationGroupPrevalence(str, Enum):
    # Indicates that we have a high prevalence in the correlation between the anomaly and correlation group.
    High = "high",
    # Indicates that we have a medium prevalence in the correlation between the anomaly and correlation group.
    Medium = "medium",
    # Indicates that we have a low prevalence in the correlation between the anomaly and correlation group.
    Low = "low",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

