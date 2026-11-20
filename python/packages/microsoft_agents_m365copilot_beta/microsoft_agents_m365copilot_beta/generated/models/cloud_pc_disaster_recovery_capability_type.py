from enum import Enum

class CloudPcDisasterRecoveryCapabilityType(str, Enum):
    None_ = "none",
    Failover = "failover",
    Failback = "failback",
    UnknownFutureValue = "unknownFutureValue",

