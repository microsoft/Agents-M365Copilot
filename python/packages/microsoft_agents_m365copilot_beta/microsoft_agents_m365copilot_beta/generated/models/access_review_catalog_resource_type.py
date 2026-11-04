from enum import Enum

class AccessReviewCatalogResourceType(str, Enum):
    None_ = "none",
    AccessPackage = "accessPackage",
    UnknownFutureValue = "unknownFutureValue",

