from enum import Enum

class LifecyclePolicyImpactActionType(str, Enum):
    ObjectCoveredByPolicy = "objectCoveredByPolicy",
    AttestationNeededWarning = "attestationNeededWarning",
    AttestationNeededNotificationSent = "attestationNeededNotificationSent",
    DisabledDueToAttestationNonCompliance = "disabledDueToAttestationNonCompliance",
    DeletedDueToAttestationNonCompliance = "deletedDueToAttestationNonCompliance",
    UnknownFutureValue = "unknownFutureValue",

