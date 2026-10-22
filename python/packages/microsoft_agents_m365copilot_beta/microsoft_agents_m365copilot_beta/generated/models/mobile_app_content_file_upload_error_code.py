from enum import Enum

class MobileAppContentFileUploadErrorCode(str, Enum):
    ApkIsInvalid = "apkIsInvalid",
    ApkIsMissingSignerCertificates = "apkIsMissingSignerCertificates",
    ApkHasInvalidPackageName = "apkHasInvalidPackageName",
    ApkPackageNameMismatch = "apkPackageNameMismatch",
    ApkHasInvalidVersionCode = "apkHasInvalidVersionCode",
    ApkHasVersionCodeMismatch = "apkHasVersionCodeMismatch",
    ApkHasInvalidMinSdk = "apkHasInvalidMinSdk",
    ApkMinSdkMismatch = "apkMinSdkMismatch",
    ApkVersionNameMismatch = "apkVersionNameMismatch",
    UnknownFutureValue = "unknownFutureValue",

