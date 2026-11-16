from enum import Enum

class DeviceManagementConfigurationAzureAdTrustType(str, Enum):
    # No AAD Trust Type specified
    None_ = "none",
    # AAD Joined Trust Type
    AzureAdJoined = "azureAdJoined",
    # AddWorkAccount
    AddWorkAccount = "addWorkAccount",
    # MDM only
    MdmOnly = "mdmOnly",

