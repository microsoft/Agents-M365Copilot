from enum import Enum

class MobileAppSupersedenceType(str, Enum):
    # Indicates that the child app should be updated by the internal logic of the parent app.
    Update = "update",
    # Indicates that the child app should be uninstalled before installing the parent app.
    Replace = "replace",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

