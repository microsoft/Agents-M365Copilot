from enum import Enum

class PolicyCategory(str, Enum):
    NotSpecified = "notSpecified",
    WorkloadIdentity = "workloadIdentity",
    IdentityAndTenant = "identityAndTenant",
    PrivilegedAccess = "privilegedAccess",
    ZeroTrust = "zeroTrust",
    AgenticIdentity = "agenticIdentity",
    NetworkAccess = "networkAccess",
    UnknownFutureValue = "unknownFutureValue",

