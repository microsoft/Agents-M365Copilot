from enum import Enum

class DhGroup(str, Enum):
    DhGroup14 = "dhGroup14",
    DhGroup24 = "dhGroup24",
    DhGroup2048 = "dhGroup2048",
    Ecp256 = "ecp256",
    Ecp384 = "ecp384",
    UnknownFutureValue = "unknownFutureValue",

