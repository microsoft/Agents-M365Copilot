from enum import Enum

class LocalSecurityOptionsAdministratorElevationPromptBehaviorType(str, Enum):
    # Not Configured
    NotConfigured = "notConfigured",
    # Elevate without prompting.
    ElevateWithoutPrompting = "elevateWithoutPrompting",
    # Prompt for credentials on the secure desktop
    PromptForCredentialsOnTheSecureDesktop = "promptForCredentialsOnTheSecureDesktop",
    # Prompt for consent on the secure desktop
    PromptForConsentOnTheSecureDesktop = "promptForConsentOnTheSecureDesktop",
    # Prompt for credentials
    PromptForCredentials = "promptForCredentials",
    # Prompt for consent
    PromptForConsent = "promptForConsent",
    # Prompt for consent for non-Windows binaries
    PromptForConsentForNonWindowsBinaries = "promptForConsentForNonWindowsBinaries",

