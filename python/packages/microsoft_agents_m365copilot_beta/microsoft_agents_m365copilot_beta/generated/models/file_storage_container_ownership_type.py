from enum import Enum

class FileStorageContainerOwnershipType(str, Enum):
    TenantOwned = "tenantOwned",
    UserOwned = "userOwned",
    UnknownFutureValue = "unknownFutureValue",

