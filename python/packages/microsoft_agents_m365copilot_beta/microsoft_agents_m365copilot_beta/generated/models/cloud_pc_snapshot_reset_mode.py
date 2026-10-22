from enum import Enum

class CloudPcSnapshotResetMode(str, Enum):
    NotApplicable = "notApplicable",
    Enabled = "enabled",
    Disabled = "disabled",
    UnknownFutureValue = "unknownFutureValue",

