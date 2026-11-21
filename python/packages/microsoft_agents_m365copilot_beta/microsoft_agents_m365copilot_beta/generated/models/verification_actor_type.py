from enum import Enum

class VerificationActorType(str, Enum):
    User = "user",
    Application = "application",
    UnknownFutureValue = "unknownFutureValue",

