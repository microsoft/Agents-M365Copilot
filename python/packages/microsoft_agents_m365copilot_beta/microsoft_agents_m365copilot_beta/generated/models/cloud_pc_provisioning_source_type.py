from enum import Enum

class CloudPcProvisioningSourceType(str, Enum):
    Image = "image",
    Snapshot = "snapshot",
    UnknownFutureValue = "unknownFutureValue",

