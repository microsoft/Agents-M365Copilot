from enum import Enum

class DeviceScopeParameter(str, Enum):
    # Device Scope parameter is not set
    None_ = "none",
    # use Scope Tag as parameter for the device scope configuration.
    ScopeTag = "scopeTag",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

