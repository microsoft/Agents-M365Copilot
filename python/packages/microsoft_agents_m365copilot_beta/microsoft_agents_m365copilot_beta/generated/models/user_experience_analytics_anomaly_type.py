from enum import Enum

class UserExperienceAnalyticsAnomalyType(str, Enum):
    # Indicates the detected anomaly is due to certain devices.
    Device = "device",
    # Indicates the detected anomaly is due to a specific application.
    Application = "application",
    # Indicates the detected anomaly is due to a specific stop error.
    StopError = "stopError",
    # Indicates the detected anomaly is due to a specific driver.
    Driver = "driver",
    # Indicates the category of detected anomaly is undefined.
    Other = "other",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

