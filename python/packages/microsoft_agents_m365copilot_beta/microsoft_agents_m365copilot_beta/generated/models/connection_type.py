from enum import Enum

class ConnectionType(str, Enum):
    WebSocket = "webSocket",
    UnknownFutureValue = "unknownFutureValue",

