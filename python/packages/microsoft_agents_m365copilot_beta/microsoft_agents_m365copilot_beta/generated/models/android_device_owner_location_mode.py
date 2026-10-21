from enum import Enum

class AndroidDeviceOwnerLocationMode(str, Enum):
    # No restrictions on the location setting and no specific behavior is set or enforced. This is the default
    NotConfigured = "notConfigured",
    # Location setting is disabled on the device
    Disabled = "disabled",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

