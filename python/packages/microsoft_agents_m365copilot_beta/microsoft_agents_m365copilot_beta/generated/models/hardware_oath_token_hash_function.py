from enum import Enum

class HardwareOathTokenHashFunction(str, Enum):
    Hmacsha1 = "hmacsha1",
    Hmacsha256 = "hmacsha256",
    UnknownFutureValue = "unknownFutureValue",

