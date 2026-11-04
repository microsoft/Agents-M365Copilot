from enum import Enum

class IncidentTaskActionType(str, Enum):
    Text = "text",
    IsolateDevice = "isolateDevice",
    StopAndQuarantineFile = "stopAndQuarantineFile",
    RunAntiVirusScan = "runAntiVirusScan",
    CollectInvestigationPackage = "collectInvestigationPackage",
    RestrictAppExecution = "restrictAppExecution",
    SubmitIocRule = "submitIocRule",
    ForceUserPasswordReset = "forceUserPasswordReset",
    DisableUser = "disableUser",
    MarkUserAsCompromised = "markUserAsCompromised",
    RequireSignIn = "requireSignIn",
    HardDeleteEmail = "hardDeleteEmail",
    SoftDeleteEmail = "softDeleteEmail",
    UnIsolateDevice = "unIsolateDevice",
    UnRestrictAppExecution = "unRestrictAppExecution",
    EnableUser = "enableUser",
    UnknownFutureValue = "unknownFutureValue",

