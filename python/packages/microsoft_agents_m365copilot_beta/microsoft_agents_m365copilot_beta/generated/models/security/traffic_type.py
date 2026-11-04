from enum import Enum

class TrafficType(str, Enum):
    DownloadedBytes = "downloadedBytes",
    UploadedBytes = "uploadedBytes",
    Unknown = "unknown",
    UnknownFutureValue = "unknownFutureValue",

