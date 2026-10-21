from enum import Enum

class CloudPcProvisioningType(str, Enum):
    Dedicated = "dedicated",
    Shared = "shared",
    UnknownFutureValue = "unknownFutureValue",
    SharedByUser = "sharedByUser",
    SharedByEntraGroup = "sharedByEntraGroup",
    Reserve = "reserve",

