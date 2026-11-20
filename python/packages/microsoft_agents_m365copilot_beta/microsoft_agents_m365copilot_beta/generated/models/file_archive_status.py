from enum import Enum

class FileArchiveStatus(str, Enum):
    NotArchived = "notArchived",
    FullyArchived = "fullyArchived",
    Reactivating = "reactivating",
    UnknownFutureValue = "unknownFutureValue",

