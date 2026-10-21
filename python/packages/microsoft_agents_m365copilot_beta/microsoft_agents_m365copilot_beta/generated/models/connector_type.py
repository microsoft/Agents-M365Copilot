from enum import Enum

class ConnectorType(str, Enum):
    SapIag = "sapIag",
    SapAc = "sapAc",
    UnknownFutureValue = "unknownFutureValue",

