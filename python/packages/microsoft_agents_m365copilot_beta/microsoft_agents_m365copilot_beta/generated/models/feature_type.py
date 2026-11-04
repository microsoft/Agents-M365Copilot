from enum import Enum

class FeatureType(str, Enum):
    Registration = "registration",
    Reset = "reset",
    UnknownFutureValue = "unknownFutureValue",

