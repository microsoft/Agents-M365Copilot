from enum import Enum

class SecurityRequirementType(str, Enum):
    MfaEnforcedForAdmins = "mfaEnforcedForAdmins",
    MfaEnforcedForAdminsOfCustomers = "mfaEnforcedForAdminsOfCustomers",
    SecurityAlertsPromptlyResolved = "securityAlertsPromptlyResolved",
    SecurityContactProvided = "securityContactProvided",
    SpendingBudgetSetForCustomerAzureSubscriptions = "spendingBudgetSetForCustomerAzureSubscriptions",
    UnknownFutureValue = "unknownFutureValue",

