from enum import Enum

class SensitiveTypeSource(str, Enum):
    OutOfBox = "outOfBox",
    Tenant = "tenant",

