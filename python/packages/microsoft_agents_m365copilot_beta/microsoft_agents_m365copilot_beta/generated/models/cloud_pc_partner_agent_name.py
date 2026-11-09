from enum import Enum

class CloudPcPartnerAgentName(str, Enum):
    Citrix = "citrix",
    UnknownFutureValue = "unknownFutureValue",
    VMware = "vMware",
    Hp = "hp",

