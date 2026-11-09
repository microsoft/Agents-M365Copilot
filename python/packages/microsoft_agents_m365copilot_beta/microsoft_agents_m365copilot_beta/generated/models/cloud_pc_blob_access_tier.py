from enum import Enum

class CloudPcBlobAccessTier(str, Enum):
    Hot = "hot",
    Cool = "cool",
    Cold = "cold",
    Archive = "archive",
    UnknownFutureValue = "unknownFutureValue",

