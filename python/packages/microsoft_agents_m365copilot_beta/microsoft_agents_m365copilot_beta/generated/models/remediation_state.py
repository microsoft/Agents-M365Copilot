from enum import Enum

class RemediationState(str, Enum):
    # Unknown result.
    Unknown = "unknown",
    # Remediation script execution was skipped
    Skipped = "skipped",
    # Remediation script executed successfully and remediated the device state
    Success = "success",
    # Remediation script executed successfully but failed to remediated the device state
    RemediationFailed = "remediationFailed",
    # Remediation script execution encountered and error or timed out
    ScriptError = "scriptError",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

