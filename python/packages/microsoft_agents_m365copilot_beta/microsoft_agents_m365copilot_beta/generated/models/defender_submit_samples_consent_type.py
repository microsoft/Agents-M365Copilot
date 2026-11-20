from enum import Enum

class DefenderSubmitSamplesConsentType(str, Enum):
    # Send safe samples automatically
    SendSafeSamplesAutomatically = "sendSafeSamplesAutomatically",
    # Always prompt
    AlwaysPrompt = "alwaysPrompt",
    # Never send
    NeverSend = "neverSend",
    # Send all samples automatically
    SendAllSamplesAutomatically = "sendAllSamplesAutomatically",

