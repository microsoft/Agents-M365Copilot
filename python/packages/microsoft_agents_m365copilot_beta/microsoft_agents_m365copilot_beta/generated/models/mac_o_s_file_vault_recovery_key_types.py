from enum import Enum

class MacOSFileVaultRecoveryKeyTypes(str, Enum):
    # Device default value, no intent.
    NotConfigured = "notConfigured",
    # An institutional recovery key is like a “master” recovery key that can be used to unlock any device whose password has been lost.
    InstitutionalRecoveryKey = "institutionalRecoveryKey",
    # A personal recovery key is a unique code that can be used to unlock the user’s device, even if the password to the device is lost.
    PersonalRecoveryKey = "personalRecoveryKey",

