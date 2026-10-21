from enum import Enum

class VerifiedIdMethodType(str, Enum):
    IdentityVerificationPartner = "identityVerificationPartner",
    TenantCustomCredential = "tenantCustomCredential",
    VerifiedEmployee = "verifiedEmployee",
    UnknownFutureValue = "unknownFutureValue",
    NotConfigured = "notConfigured",

