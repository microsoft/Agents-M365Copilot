from enum import Enum

class SecureAssessmentAccountType(str, Enum):
    # Indicates an Azure AD account in format of AzureAD/username@tenant.com.
    AzureADAccount = "azureADAccount",
    # Indicates a domain account in format of domain/user or user@domain.com.
    DomainAccount = "domainAccount",
    # Indicates a local account in format of username.
    LocalAccount = "localAccount",
    # Indicates a local guest account in format of test name.
    LocalGuestAccount = "localGuestAccount",

