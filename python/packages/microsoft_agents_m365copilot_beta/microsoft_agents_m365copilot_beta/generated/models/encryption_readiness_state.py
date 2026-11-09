from enum import Enum

class EncryptionReadinessState(str, Enum):
    # Not ready
    NotReady = "notReady",
    # Ready
    Ready = "ready",

