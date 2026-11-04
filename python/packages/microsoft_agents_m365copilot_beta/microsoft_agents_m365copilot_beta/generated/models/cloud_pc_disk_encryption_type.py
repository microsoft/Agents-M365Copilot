from enum import Enum

class CloudPcDiskEncryptionType(str, Enum):
    PlatformManagedKey = "platformManagedKey",
    CustomerManagedKey = "customerManagedKey",
    UnknownFutureValue = "unknownFutureValue",

