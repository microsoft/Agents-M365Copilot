from enum import Enum

class DocumentProcessingJobType(str, Enum):
    File = "file",
    Folder = "folder",
    UnknownFutureValue = "unknownFutureValue",

