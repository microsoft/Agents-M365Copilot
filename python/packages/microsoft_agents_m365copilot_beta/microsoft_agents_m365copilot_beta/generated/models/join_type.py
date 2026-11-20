from enum import Enum

class JoinType(str, Enum):
    # Unknown enrollment join type.
    Unknown = "unknown",
    # The device is joined by Azure AD.
    AzureADJoined = "azureADJoined",
    # The device is registered by Azure AD.
    AzureADRegistered = "azureADRegistered",
    # The device is joined by hybrid Azure AD.
    HybridAzureADJoined = "hybridAzureADJoined",

