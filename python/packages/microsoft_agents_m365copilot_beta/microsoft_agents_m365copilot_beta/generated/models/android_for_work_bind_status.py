from enum import Enum

class AndroidForWorkBindStatus(str, Enum):
    NotBound = "notBound",
    Bound = "bound",
    BoundAndValidated = "boundAndValidated",
    Unbinding = "unbinding",

