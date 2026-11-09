from enum import Enum

class AppInstallControlType(str, Enum):
    # Not configured
    NotConfigured = "notConfigured",
    # Turn off app recommendations
    Anywhere = "anywhere",
    # Allow apps from Store only
    StoreOnly = "storeOnly",
    # Show me app recommendations
    Recommendations = "recommendations",
    # Warn me before installing apps from outside the Store
    PreferStore = "preferStore",

