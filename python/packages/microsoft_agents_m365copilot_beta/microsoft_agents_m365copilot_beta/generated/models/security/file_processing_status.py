from enum import Enum

class FileProcessingStatus(str, Enum):
    Success = "success",
    InternalError = "internalError",
    UnknownError = "unknownError",
    ProcessingTimeout = "processingTimeout",
    InvalidFileId = "invalidFileId",
    FileSizeIsZero = "fileSizeIsZero",
    FileSizeIsTooLarge = "fileSizeIsTooLarge",
    FileDepthLimitExceeded = "fileDepthLimitExceeded",
    FileBodyIsTooLong = "fileBodyIsTooLong",
    FileTypeIsUnknown = "fileTypeIsUnknown",
    FileTypeIsNotSupported = "fileTypeIsNotSupported",
    MalformedFile = "malformedFile",
    ProtectedFile = "protectedFile",
    PoisonFile = "poisonFile",
    NoReviewSetSummaryGenerated = "noReviewSetSummaryGenerated",
    ExtractionException = "extractionException",
    OcrProcessingTimeout = "ocrProcessingTimeout",
    OcrFileSizeExceedsLimit = "ocrFileSizeExceedsLimit",
    UnknownFutureValue = "unknownFutureValue",

