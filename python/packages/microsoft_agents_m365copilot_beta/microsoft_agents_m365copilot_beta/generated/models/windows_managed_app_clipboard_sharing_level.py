from enum import Enum

class WindowsManagedAppClipboardSharingLevel(str, Enum):
    # Org users can paste data from and cut/copy data to any account, document, location or application.
    AnyDestinationAnySource = "anyDestinationAnySource",
    # Org users cannot cut, copy or paste data to or from external accounts, documents, locations or applications from or into the org context.
    None_ = "none",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

