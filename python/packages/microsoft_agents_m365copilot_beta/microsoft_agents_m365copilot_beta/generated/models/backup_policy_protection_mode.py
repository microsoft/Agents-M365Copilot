from enum import Enum

class BackupPolicyProtectionMode(str, Enum):
    Standard = "standard",
    FullServiceBackup = "fullServiceBackup",
    UnknownFutureValue = "unknownFutureValue",

