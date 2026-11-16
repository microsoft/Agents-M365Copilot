from enum import Enum

class TlpLevel(str, Enum):
    Unknown = "unknown",
    White = "white",
    Green = "green",
    Amber = "amber",
    Red = "red",
    UnknownFutureValue = "unknownFutureValue",

