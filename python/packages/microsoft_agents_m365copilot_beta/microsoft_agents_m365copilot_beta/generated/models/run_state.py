from enum import Enum

class RunState(str, Enum):
    # Unknown result.
    Unknown = "unknown",
    # Script is run successfully.
    Success = "success",
    # Script failed to run.
    Fail = "fail",
    # Discovery script hits error.
    ScriptError = "scriptError",
    # Script is pending to execute.
    Pending = "pending",
    # Script is not applicable for this device.
    NotApplicable = "notApplicable",

