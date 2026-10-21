from enum import Enum

class WindowsQualityUpdateCadence(str, Enum):
    # Default. Indicates the quality update is released in a regular monthly pattern.
    Monthly = "monthly",
    # Indicates the quality update is released in an out-of-band pattern.
    OutOfBand = "outOfBand",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

