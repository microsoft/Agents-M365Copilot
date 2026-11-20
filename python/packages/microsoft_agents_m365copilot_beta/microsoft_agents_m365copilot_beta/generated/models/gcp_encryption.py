from enum import Enum

class GcpEncryption(str, Enum):
    Google = "google",
    Customer = "customer",
    UnknownFutureValue = "unknownFutureValue",

