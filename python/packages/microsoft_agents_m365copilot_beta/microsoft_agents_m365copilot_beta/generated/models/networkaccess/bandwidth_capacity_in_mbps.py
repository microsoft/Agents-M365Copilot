from enum import Enum

class BandwidthCapacityInMbps(str, Enum):
    Mbps250 = "mbps250",
    Mbps500 = "mbps500",
    Mbps750 = "mbps750",
    Mbps1000 = "mbps1000",
    UnknownFutureValue = "unknownFutureValue",

