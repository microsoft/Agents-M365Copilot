from enum import Enum

class PrivilegeManagementEndUserType(str, Enum):
    # Default. Unable to determine the login type of the user.
    Undetermined = "undetermined",
    # The user who performed the elevation logged in using an Azure Active Directory (Azure AD) account.
    AzureAd = "azureAd",
    # The user who performed the elevation logged in using Hybrid Azure AD joined account.
    Hybrid = "hybrid",
    # The user who performed the elevation logged in using a Windows local account.
    Local = "local",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

