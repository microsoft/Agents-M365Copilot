from enum import Enum

class UserExperienceAnalyticsAnomalyDeviceFeatureType(str, Enum):
    # Indicates the manufacturer name as device feature type.
    Manufacturer = "manufacturer",
    # Indicates the model as a device feature type.
    Model = "model",
    # Indicates the OS as a device feature type.
    OsVersion = "osVersion",
    # Indicates the application as a device feature type.
    Application = "application",
    # Indicates the driver as a device feature type.
    Driver = "driver",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

