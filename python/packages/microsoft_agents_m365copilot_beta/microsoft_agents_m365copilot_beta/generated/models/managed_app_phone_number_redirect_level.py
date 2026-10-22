from enum import Enum

class ManagedAppPhoneNumberRedirectLevel(str, Enum):
    # Sharing is allowed to all apps.
    AllApps = "allApps",
    # Sharing is allowed to all managed apps.
    ManagedApps = "managedApps",
    # Sharing is allowed to a custom app.
    CustomApp = "customApp",
    # Sharing between apps is blocked.
    Blocked = "blocked",

