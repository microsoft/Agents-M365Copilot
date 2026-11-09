from enum import Enum

class CloudPcGeographicLocationType(str, Enum):
    Default = "default",
    Asia = "asia",
    Australasia = "australasia",
    Canada = "canada",
    Europe = "europe",
    India = "india",
    Africa = "africa",
    UsCentral = "usCentral",
    UsEast = "usEast",
    UsWest = "usWest",
    SouthAmerica = "southAmerica",
    MiddleEast = "middleEast",
    CentralAmerica = "centralAmerica",
    UsGovernment = "usGovernment",
    UnknownFutureValue = "unknownFutureValue",
    Mexico = "mexico",
    AustraliaNewZealand = "australiaNewZealand",

