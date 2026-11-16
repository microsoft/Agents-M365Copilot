from enum import Enum

class CloudPcUserSettingsPersistenceSnapshotType(str, Enum):
    Automatic = "automatic",
    Manual = "manual",
    UnknownFutureValue = "unknownFutureValue",

