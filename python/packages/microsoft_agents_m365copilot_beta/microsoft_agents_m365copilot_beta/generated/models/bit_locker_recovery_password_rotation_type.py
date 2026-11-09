from enum import Enum

class BitLockerRecoveryPasswordRotationType(str, Enum):
    # Not configured
    NotConfigured = "notConfigured",
    # Recovery password rotation off
    Disabled = "disabled",
    # Recovery password rotation on for Azure AD joined devices
    EnabledForAzureAd = "enabledForAzureAd",
    # Recovery password rotation on for both Azure AD joined and hybrid joined devices
    EnabledForAzureAdAndHybrid = "enabledForAzureAdAndHybrid",

