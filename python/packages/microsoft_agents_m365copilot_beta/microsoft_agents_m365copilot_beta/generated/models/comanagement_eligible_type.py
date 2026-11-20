from enum import Enum

class ComanagementEligibleType(str, Enum):
    Comanaged = "comanaged",
    Eligible = "eligible",
    EligibleButNotAzureAdJoined = "eligibleButNotAzureAdJoined",
    NeedsOsUpdate = "needsOsUpdate",
    Ineligible = "ineligible",
    # Devices scheduled for Co-Management enrollment
    ScheduledForEnrollment = "scheduledForEnrollment",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

