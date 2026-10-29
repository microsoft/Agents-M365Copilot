from enum import Enum

class DeviceEventLevel(str, Enum):
    # Indicates that the device event level is none.
    None_ = "none",
    # Indicates that the device event level is verbose.
    Verbose = "verbose",
    # Indicates that the device event level is information.
    Information = "information",
    # Indicates that the device event level is warning.
    Warning = "warning",
    # Indicates that the device event level is error.
    Error = "error",
    # Indicates that the device event level is critical.
    Critical = "critical",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

