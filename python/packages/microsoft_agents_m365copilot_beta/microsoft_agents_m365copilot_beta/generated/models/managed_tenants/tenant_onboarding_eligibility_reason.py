from enum import Enum

class TenantOnboardingEligibilityReason(str, Enum):
    None_ = "none",
    ContractType = "contractType",
    DelegatedAdminPrivileges = "delegatedAdminPrivileges",
    UsersCount = "usersCount",
    License = "license",
    UnknownFutureValue = "unknownFutureValue",

