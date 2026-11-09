from enum import Enum

class CloudPcPowerState(str, Enum):
    Running = "running",
    PoweredOff = "poweredOff",
    UnknownFutureValue = "unknownFutureValue",

