from enum import Enum

class StopAndQuarantineFileEntityIdentifier(str, Enum):
    DeviceId = "deviceId",
    Sha1 = "sha1",
    InitiatingProcessSHA1 = "initiatingProcessSHA1",
    UnknownFutureValue = "unknownFutureValue",

