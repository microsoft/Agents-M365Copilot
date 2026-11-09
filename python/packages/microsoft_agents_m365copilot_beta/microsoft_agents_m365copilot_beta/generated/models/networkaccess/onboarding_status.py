from enum import Enum

class OnboardingStatus(str, Enum):
    Offboarded = "offboarded",
    OffboardingInProgress = "offboardingInProgress",
    OnboardingInProgress = "onboardingInProgress",
    Onboarded = "onboarded",
    OnboardingErrorOccurred = "onboardingErrorOccurred",
    OffboardingErrorOccurred = "offboardingErrorOccurred",
    UnknownFutureValue = "unknownFutureValue",

