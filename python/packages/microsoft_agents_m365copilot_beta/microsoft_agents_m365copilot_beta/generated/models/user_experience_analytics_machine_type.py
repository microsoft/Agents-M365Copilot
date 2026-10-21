from enum import Enum

class UserExperienceAnalyticsMachineType(str, Enum):
    # Indicates that the type is unknown.
    Unknown = "unknown",
    # Indicates that the Machine is physical.
    Physical = "physical",
    # Indicates that the machine is virtual.
    Virtual = "virtual",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

