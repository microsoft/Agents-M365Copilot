from enum import Enum

class PhysicalAddressType(str, Enum):
    Unknown = "unknown",
    Home = "home",
    Business = "business",
    Other = "other",

