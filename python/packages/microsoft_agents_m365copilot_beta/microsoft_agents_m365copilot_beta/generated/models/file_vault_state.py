from enum import Enum

class FileVaultState(str, Enum):
    # FileVault State Success
    Success = "success",
    # FileVault has been enabled by user and is not being managed by policy
    DriveEncryptedByUser = "driveEncryptedByUser",
    # FileVault policy is successfully installed but user has not started encryption
    UserDeferredEncryption = "userDeferredEncryption",
    # FileVault recovery key escrow is not enabled
    EscrowNotEnabled = "escrowNotEnabled",

