from enum import Enum

class DelegatedPrivilegeStatus(str, Enum):
    None_ = "none",
    DelegatedAdminPrivileges = "delegatedAdminPrivileges",
    UnknownFutureValue = "unknownFutureValue",
    GranularDelegatedAdminPrivileges = "granularDelegatedAdminPrivileges",
    DelegatedAndGranularDelegetedAdminPrivileges = "delegatedAndGranularDelegetedAdminPrivileges",

