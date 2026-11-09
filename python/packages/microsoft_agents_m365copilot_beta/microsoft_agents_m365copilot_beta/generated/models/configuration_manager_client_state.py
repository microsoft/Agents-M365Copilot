from enum import Enum

class ConfigurationManagerClientState(str, Enum):
    # Configuration manager agent is older than 1806 or not installed or this device has not checked into Intune for over 30 days.
    Unknown = "unknown",
    # The configuration manager agent is installed but may not be showing up in the configuration manager console yet. Wait a few hours for it to refresh.
    Installed = "installed",
    # This device was able to check in with the configuration manager service successfully.
    Healthy = "healthy",
    # The configuration manager agent failed to install.
    InstallFailed = "installFailed",
    # The update from version x to version y of the configuration manager agent failed. 
    UpdateFailed = "updateFailed",
    # The configuration manager agent was able to reach the configuration manager service in the past but is now no longer able to. 
    CommunicationError = "communicationError",

