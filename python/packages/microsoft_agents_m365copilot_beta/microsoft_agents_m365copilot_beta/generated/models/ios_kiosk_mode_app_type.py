from enum import Enum

class IosKioskModeAppType(str, Enum):
    # Device default value, no intent.
    NotConfigured = "notConfigured",
    # The app to be run comes from the app store.
    AppStoreApp = "appStoreApp",
    # The app to be run is built into the device.
    ManagedApp = "managedApp",
    # The app to be run is a managed app.
    BuiltInApp = "builtInApp",

