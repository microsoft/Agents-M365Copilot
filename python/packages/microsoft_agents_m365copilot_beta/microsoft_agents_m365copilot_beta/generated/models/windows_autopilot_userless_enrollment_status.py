from enum import Enum

class WindowsAutopilotUserlessEnrollmentStatus(str, Enum):
    # Unknown userless enrollment block status. Next userless enrollment may fail. This is the default value.
    Unknown = "unknown",
    # Indicates next userless enrollment can proceed.
    Allowed = "allowed",
    # Indicates next userless enrollment cannot proceed without resetting the windowsAutopilotUserlessEnrollmentStatus.
    Blocked = "blocked",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

