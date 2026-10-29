from enum import Enum

class BalanceEvaluationFailureReason(str, Enum):
    # The service could not resolve the spending policy, so no authoritative balance or accessdecision could be produced.
    UpstreamFailure = "upstreamFailure",
    # No spending policy governs this service for this user, so there is no balance to report.Retrying does not change this until a policy is created for the service, or the user isbrought into an existing policy's scope.
    NoApplicablePolicy = "noApplicablePolicy",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

