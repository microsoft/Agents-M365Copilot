from enum import Enum

class ProvenanceActorType(str, Enum):
    System = "system",
    User = "user",
    Application = "application",
    UnknownFutureValue = "unknownFutureValue",

