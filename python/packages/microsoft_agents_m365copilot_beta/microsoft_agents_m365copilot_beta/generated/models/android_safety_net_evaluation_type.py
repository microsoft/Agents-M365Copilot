from enum import Enum

class AndroidSafetyNetEvaluationType(str, Enum):
    # Default value. Typical measurements and reference data were used.
    Basic = "basic",
    # Strong Integrity checks (such as a hardware-backed proof of boot integrity) were used.
    HardwareBacked = "hardwareBacked",

