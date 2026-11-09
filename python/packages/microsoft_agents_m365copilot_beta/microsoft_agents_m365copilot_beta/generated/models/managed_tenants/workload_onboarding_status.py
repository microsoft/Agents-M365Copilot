from enum import Enum

class WorkloadOnboardingStatus(str, Enum):
    NotOnboarded = "notOnboarded",
    Onboarded = "onboarded",
    UnknownFutureValue = "unknownFutureValue",

