from enum import Enum

class AndroidManagedStoreAutoUpdateMode(str, Enum):
    # Default update behavior (device must be connected to Wifi, charging and not actively used).
    Default = "default",
    # Updates are postponed for a maximum of 90 days after the app becomes out of date.
    Postponed = "postponed",
    # The app is updated as soon as possible by the developer. If device is online, it will be updated within minutes.
    Priority = "priority",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

