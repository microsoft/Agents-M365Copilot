from enum import Enum

class PermissionsRequestOccurrenceStatus(str, Enum):
    GrantingFailed = "grantingFailed",
    Granted = "granted",
    Granting = "granting",
    Revoked = "revoked",
    Revoking = "revoking",
    RevokingFailed = "revokingFailed",
    UnknownFutureValue = "unknownFutureValue",

