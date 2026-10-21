from enum import Enum

class UserExperienceAnalyticsDeviceStatus(str, Enum):
    # Indicates the the device is part of the anomaly.
    Anomalous = "anomalous",
    # Indicates the device is affected by the anomaly and is part of the correlation group.
    Affected = "affected",
    # Indicates the device is not part of the anomaly but is part of the correlation group.
    AtRisk = "atRisk",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

