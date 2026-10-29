from enum import Enum

class DdmAppAllowDownloadsOverCellular(str, Enum):
    # The device downloads apps of any size using a cellular network.
    AlwaysOn = "alwaysOn",
    # The device doesn't download apps using a cellular network. The device pauses the automatic install or update operation until a different network is active.
    AlwaysOff = "alwaysOff",
    # The device uses the settings for the corresponding store when downloading apps.
    StoreSettings = "storeSettings",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

