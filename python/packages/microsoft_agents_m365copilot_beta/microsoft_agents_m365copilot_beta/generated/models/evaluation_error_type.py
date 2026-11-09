from enum import Enum

class EvaluationErrorType(str, Enum):
    UnsupportedFile = "unsupportedFile",
    PasswordProtectedFile = "passwordProtectedFile",
    MissingOrInvalidConfiguration = "missingOrInvalidConfiguration",
    AgentFailure = "agentFailure",
    EnforcementTimeout = "enforcementTimeout",
    OsOverride = "osOverride",
    ProcessNonExistent = "processNonExistent",
    Other = "other",
    ServiceTimeout = "serviceTimeout",
    ServiceError = "serviceError",
    ServiceUnavailable = "serviceUnavailable",
    ContentTooLarge = "contentTooLarge",
    PartiallyScanned = "partiallyScanned",
    Unscannable = "unscannable",
    BillingNotSetup = "billingNotSetup",
    AuthenticationOrAuthorizationFailed = "authenticationOrAuthorizationFailed",
    UnknownFutureValue = "unknownFutureValue",

