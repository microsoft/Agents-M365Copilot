from enum import Enum

class DeviceServiceSubstate(str, Enum):
    Unknown = "unknown",
    Scheduled = "scheduled",
    OfferReady = "offerReady",
    AdminPaused = "adminPaused",
    AdminCancelled = "adminCancelled",
    RemovedFromDeployment = "removedFromDeployment",
    NotOffering = "notOffering",
    UnknownFutureValue = "unknownFutureValue",

