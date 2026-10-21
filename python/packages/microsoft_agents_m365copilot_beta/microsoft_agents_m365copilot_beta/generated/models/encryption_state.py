from enum import Enum

class EncryptionState(str, Enum):
    # Not encrypted
    NotEncrypted = "notEncrypted",
    # Encrypted
    Encrypted = "encrypted",

