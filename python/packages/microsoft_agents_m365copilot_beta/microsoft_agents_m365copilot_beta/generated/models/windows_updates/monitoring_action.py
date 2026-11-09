from enum import Enum

class MonitoringAction(str, Enum):
    AlertError = "alertError",
    OfferFallback = "offerFallback",
    PauseDeployment = "pauseDeployment",
    UnknownFutureValue = "unknownFutureValue",

