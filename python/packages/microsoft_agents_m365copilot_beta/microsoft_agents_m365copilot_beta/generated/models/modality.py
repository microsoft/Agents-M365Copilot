from enum import Enum

class Modality(str, Enum):
    Unknown = "unknown",
    Audio = "audio",
    Video = "video",
    VideoBasedScreenSharing = "videoBasedScreenSharing",
    Data = "data",
    UnknownFutureValue = "unknownFutureValue",

