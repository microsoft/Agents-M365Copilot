from enum import Enum

class DdmAppAutomaticAppUpdates(str, Enum):
    # The device automatically updates the app to the latest version.
    AlwaysOn = "alwaysOn",
    # The device never automatically updates the app.
    AlwaysOff = "alwaysOff",
    # The device uses the settings for the corresponding store to determine when to automatically update the app.
    StoreSettings = "storeSettings",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

