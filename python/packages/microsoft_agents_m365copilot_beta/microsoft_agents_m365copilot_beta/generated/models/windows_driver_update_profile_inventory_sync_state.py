from enum import Enum

class WindowsDriverUpdateProfileInventorySyncState(str, Enum):
    # Pending sync.
    Pending = "pending",
    # Successful sync.
    Success = "success",
    # Failed sync.
    Failure = "failure",

