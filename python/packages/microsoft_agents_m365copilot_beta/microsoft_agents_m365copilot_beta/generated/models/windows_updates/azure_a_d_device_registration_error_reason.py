from enum import Enum

class AzureADDeviceRegistrationErrorReason(str, Enum):
    InvalidGlobalDeviceId = "invalidGlobalDeviceId",
    InvalidAzureADDeviceId = "invalidAzureADDeviceId",
    MissingTrustType = "missingTrustType",
    InvalidAzureADJoin = "invalidAzureADJoin",
    UnknownFutureValue = "unknownFutureValue",

