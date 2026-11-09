from enum import Enum

class ManagedAppLogUploadState(str, Enum):
    # Default. The log upload request has been successfully created, and is pending delivery to the Mobile Application Management (MAM) application.
    Pending = "pending",
    # One or more log upload components have uploaded their logs.
    InProgress = "inProgress",
    # All log upload successfully components have uploaded their logs.
    Completed = "completed",
    # The log upload request was declined by the user on the device.
    DeclinedByUser = "declinedByUser",
    # The log upload request was not acknowledged by the user within the allowed time window.
    TimedOut = "timedOut",
    # The log upload request encountered an error.
    Failed = "failed",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

