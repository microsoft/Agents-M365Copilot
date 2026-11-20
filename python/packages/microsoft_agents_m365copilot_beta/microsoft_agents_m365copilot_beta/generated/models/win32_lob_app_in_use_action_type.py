from enum import Enum

class Win32LobAppInUseActionType(str, Enum):
    # Default. Indicates that no in-use detection will be evaluated before an app enforcement.
    NotEnabled = "notEnabled",
    # Indicates that the in-use detection will occur immediately before app enforcement. Enforcement will not occur if the app is detected to be in-use, and an error status will be reported for the app.
    Fail = "fail",
    # Indicates that in-use detection will occur immediately before app enforcement. If the app is detected to be in-use, the processes specified in the corresponding process detection rules will be terminated, and app enforcement will commence.
    TerminateWithoutUserInteraction = "terminateWithoutUserInteraction",
    # Indicates that in-use detection will occur immediately before app enforcement. If the app is detected to be in-use, the end user will be prompted according to the configured deferral and countdown settings, and the processes specified in the corresponding process detection rules will be terminated before app enforcement is commenced. If any of the processes cannot be terminated, the app will not be enforced, and an error status will be reported for the app.
    TerminateWithUserInteraction = "terminateWithUserInteraction",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

