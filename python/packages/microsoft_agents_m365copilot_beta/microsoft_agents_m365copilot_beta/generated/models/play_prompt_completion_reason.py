from enum import Enum

class PlayPromptCompletionReason(str, Enum):
    Unknown = "unknown",
    CompletedSuccessfully = "completedSuccessfully",
    MediaOperationCanceled = "mediaOperationCanceled",
    UnknownFutureValue = "unknownFutureValue",

