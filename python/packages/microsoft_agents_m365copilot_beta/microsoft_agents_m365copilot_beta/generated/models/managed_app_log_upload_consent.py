from enum import Enum

class ManagedAppLogUploadConsent(str, Enum):
    # Default. Indicates app log consent state is 'Unknown'. This state is automatically assigned at request creation time and is updated when the log collection completes.
    Unknown = "unknown",
    # The User has Declined the Log Collection Request. The Log collection and uploads will not be initiated/triggered, and the log collection request will be abandoned.
    Declined = "declined",
    # The User has Accepted the Log Collection Request. The log collection and upload will be initiated.
    Accepted = "accepted",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

