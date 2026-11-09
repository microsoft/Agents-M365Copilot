from enum import Enum

class AndroidManagedStoreAccountBindStatus(str, Enum):
    NotBound = "notBound",
    Bound = "bound",
    BoundAndValidated = "boundAndValidated",
    Unbinding = "unbinding",

