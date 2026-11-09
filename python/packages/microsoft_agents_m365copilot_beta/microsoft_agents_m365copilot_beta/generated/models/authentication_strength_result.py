from enum import Enum

class AuthenticationStrengthResult(str, Enum):
    NotSet = "notSet",
    SkippedForProofUp = "skippedForProofUp",
    Satisfied = "satisfied",
    SingleChallengeRequired = "singleChallengeRequired",
    MultipleChallengesRequired = "multipleChallengesRequired",
    SingleRegistrationRequired = "singleRegistrationRequired",
    MultipleRegistrationsRequired = "multipleRegistrationsRequired",
    CannotSatisfyDueToCombinationConfiguration = "cannotSatisfyDueToCombinationConfiguration",
    CannotSatisfy = "cannotSatisfy",
    UnknownFutureValue = "unknownFutureValue",

