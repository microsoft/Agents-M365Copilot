from enum import Enum

class DeploymentStateReasonValue(str, Enum):
    ScheduledByOfferWindow = "scheduledByOfferWindow",
    OfferingByRequest = "offeringByRequest",
    PausedByRequest = "pausedByRequest",
    PausedByMonitoring = "pausedByMonitoring",
    UnknownFutureValue = "unknownFutureValue",
    FaultedByContentOutdated = "faultedByContentOutdated",

