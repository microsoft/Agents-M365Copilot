from enum import Enum

class AttachmentScanResult(str, Enum):
    Unscanned = "unscanned",
    NoThreatsFound = "noThreatsFound",
    Malicious = "malicious",
    UnknownFutureValue = "unknownFutureValue",

