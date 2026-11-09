from enum import Enum

class CloudPcDeviceImageStatusDetails(str, Enum):
    InternalServerError = "internalServerError",
    SourceImageNotFound = "sourceImageNotFound",
    OsVersionNotSupported = "osVersionNotSupported",
    SourceImageInvalid = "sourceImageInvalid",
    SourceImageNotGeneralized = "sourceImageNotGeneralized",
    UnknownFutureValue = "unknownFutureValue",
    VmAlreadyAzureAdjoined = "vmAlreadyAzureAdjoined",
    PaidSourceImageNotSupport = "paidSourceImageNotSupport",
    SourceImageNotSupportCustomizeVMName = "sourceImageNotSupportCustomizeVMName",
    SourceImageSizeExceedsLimitation = "sourceImageSizeExceedsLimitation",

