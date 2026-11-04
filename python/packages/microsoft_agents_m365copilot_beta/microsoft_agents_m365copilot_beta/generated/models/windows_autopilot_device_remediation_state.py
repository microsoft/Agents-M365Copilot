from enum import Enum

class WindowsAutopilotDeviceRemediationState(str, Enum):
    # Unknown status.
    Unknown = "unknown",
    # No hardware change has been detected.
    NoRemediationRequired = "noRemediationRequired",
    # Hardware change detected on client. Additional remediation is required.
    AutomaticRemediationRequired = "automaticRemediationRequired",
    # Hardware change detected on client that could not resolved automatically. Additional remediation is required.
    ManualRemediationRequired = "manualRemediationRequired",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

