from enum import Enum

class AppInfoUploadedDataTypes(str, Enum):
    Documents = "documents",
    MediaFiles = "mediaFiles",
    CodingFiles = "codingFiles",
    CreditCards = "creditCards",
    DatabaseFiles = "databaseFiles",
    None_ = "none",
    Unknown = "unknown",
    UnknownFutureValue = "unknownFutureValue",

