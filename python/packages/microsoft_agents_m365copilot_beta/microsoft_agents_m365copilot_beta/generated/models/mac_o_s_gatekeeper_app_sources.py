from enum import Enum

class MacOSGatekeeperAppSources(str, Enum):
    # Device default value, no intent.
    NotConfigured = "notConfigured",
    # Only apps from the Mac AppStore can be run.
    MacAppStore = "macAppStore",
    # Only apps from the Mac AppStore and identified developers can be run.
    MacAppStoreAndIdentifiedDevelopers = "macAppStoreAndIdentifiedDevelopers",
    # Apps from anywhere can be run.
    Anywhere = "anywhere",

