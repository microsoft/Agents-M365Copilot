from enum import Enum

class CloudPcDiskEncryptionState(str, Enum):
    NotAvailable = "notAvailable",
    NotEncrypted = "notEncrypted",
    EncryptedUsingPlatformManagedKey = "encryptedUsingPlatformManagedKey",
    EncryptedUsingCustomerManagedKey = "encryptedUsingCustomerManagedKey",
    UnknownFutureValue = "unknownFutureValue",

