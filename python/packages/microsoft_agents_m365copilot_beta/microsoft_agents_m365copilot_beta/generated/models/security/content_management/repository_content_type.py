from enum import Enum

class RepositoryContentType(str, Enum):
    # Custom detection.
    CustomDetection = "customDetection",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",
    # Defender workbook.
    DefenderWorkbook = "defenderWorkbook",

