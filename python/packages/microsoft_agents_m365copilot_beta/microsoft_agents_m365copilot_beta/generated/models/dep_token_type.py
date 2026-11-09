from enum import Enum

class DepTokenType(str, Enum):
    # Token Type is None
    None_ = "none",
    # Token Type is Dep.
    Dep = "dep",
    # Token Type is Apple School Manager
    AppleSchoolManager = "appleSchoolManager",

