from enum import Enum

class ProvisionState(str, Enum):
    NotProvisioned = "notProvisioned",
    ProvisioningInProgress = "provisioningInProgress",
    ProvisioningFailed = "provisioningFailed",
    ProvisioningCompleted = "provisioningCompleted",
    UnknownFutureValue = "unknownFutureValue",

