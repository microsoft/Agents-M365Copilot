from enum import Enum

class CloudPcSnapshotType(str, Enum):
    Automatic = "automatic",
    Manual = "manual",
    UnknownFutureValue = "unknownFutureValue",
    Retention = "retention",

