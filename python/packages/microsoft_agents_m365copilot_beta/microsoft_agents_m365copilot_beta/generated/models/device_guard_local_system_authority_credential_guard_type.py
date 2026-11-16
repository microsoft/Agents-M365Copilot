from enum import Enum

class DeviceGuardLocalSystemAuthorityCredentialGuardType(str, Enum):
    # Turns off Credential Guard remotely if configured previously without UEFI Lock.
    NotConfigured = "notConfigured",
    # Turns on Credential Guard with UEFI lock.
    EnableWithUEFILock = "enableWithUEFILock",
    # Turns on Credential Guard without UEFI lock.
    EnableWithoutUEFILock = "enableWithoutUEFILock",
    # Disables Credential Guard. This is the default OS value.
    Disable = "disable",

