from enum import Enum

class AndroidManagedAppSafetyNetEvaluationType(str, Enum):
    # Require basic evaluation
    Basic = "basic",
    # Require hardware backed evaluation
    HardwareBacked = "hardwareBacked",

