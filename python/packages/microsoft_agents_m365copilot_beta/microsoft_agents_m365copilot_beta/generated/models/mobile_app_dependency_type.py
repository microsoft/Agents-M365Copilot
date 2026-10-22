from enum import Enum

class MobileAppDependencyType(str, Enum):
    # Indicates that the child app should be detected before installing the parent app.
    Detect = "detect",
    # Indicates that the child app should be installed before installing the parent app.
    AutoInstall = "autoInstall",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

