from enum import Enum

class DeviceType(str, Enum):
    DomainController = "domainController",
    Adfs = "adfs",
    Adcs = "adcs",
    EntraConnect = "entraConnect",
    UnknownFutureValue = "unknownFutureValue",

