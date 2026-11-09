from enum import Enum

class RestrictedAppsState(str, Enum):
    # Prohibited apps
    ProhibitedApps = "prohibitedApps",
    # Not approved apps
    NotApprovedApps = "notApprovedApps",

