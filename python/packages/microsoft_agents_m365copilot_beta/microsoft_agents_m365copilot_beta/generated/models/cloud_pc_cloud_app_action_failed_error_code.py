from enum import Enum

class CloudPcCloudAppActionFailedErrorCode(str, Enum):
    CloudAppQuotaExceeded = "cloudAppQuotaExceeded",
    CloudPcLicenseNotFound = "cloudPcLicenseNotFound",
    InternalServerError = "internalServerError",
    AppDiscoveryFailed = "appDiscoveryFailed",
    UnknownFutureValue = "unknownFutureValue",
    IconPathInvalid = "iconPathInvalid",
    FilePathInvalid = "filePathInvalid",

