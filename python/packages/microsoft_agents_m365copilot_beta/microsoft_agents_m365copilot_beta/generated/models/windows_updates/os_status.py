from enum import Enum

class OsStatus(str, Enum):
    EndOfServicing = "endOfServicing",
    InServicing = "inServicing",
    NearEndOfServicing = "nearEndOfServicing",
    UnknownFutureValue = "unknownFutureValue",

