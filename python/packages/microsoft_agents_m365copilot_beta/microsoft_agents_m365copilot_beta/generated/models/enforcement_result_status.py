from enum import Enum

class EnforcementResultStatus(str, Enum):
    Success = "success",
    MissingOrInvalidConfiguration = "missingOrInvalidConfiguration",
    UserOverride = "userOverride",
    AgentFailure = "agentFailure",
    EnforcementTimeout = "enforcementTimeout",
    OSOverride = "oSOverride",
    ProcessNonExistent = "processNonExistent",
    Other = "other",

