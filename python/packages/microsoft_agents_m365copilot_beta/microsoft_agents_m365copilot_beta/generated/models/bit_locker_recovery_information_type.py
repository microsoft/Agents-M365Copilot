from enum import Enum

class BitLockerRecoveryInformationType(str, Enum):
    # Store recovery passwords and key packages.
    PasswordAndKey = "passwordAndKey",
    # Store recovery passwords only.
    PasswordOnly = "passwordOnly",

