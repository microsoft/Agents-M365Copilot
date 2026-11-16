from enum import Enum

class UserExperienceAnalyticsAnomalySeverity(str, Enum):
    # Indicates the anomaly is of high severity.
    High = "high",
    # Indicates the anomaly is of medium severity.
    Medium = "medium",
    # Indicates the anomaly is of low severity.
    Low = "low",
    # Indicates the anomaly is of informational severity.
    Informational = "informational",
    # Indicates the severity of anomaly is undefined.
    Other = "other",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

