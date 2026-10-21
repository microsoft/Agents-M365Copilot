from enum import Enum

class SetupStatus(str, Enum):
    Unknown = "unknown",
    NotRegisteredYet = "notRegisteredYet",
    RegisteredSetupNotStarted = "registeredSetupNotStarted",
    RegisteredSetupInProgress = "registeredSetupInProgress",
    RegistrationAndSetupCompleted = "registrationAndSetupCompleted",
    RegistrationFailed = "registrationFailed",
    RegistrationTimedOut = "registrationTimedOut",
    Disabled = "disabled",

