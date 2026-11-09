from enum import Enum

class WindowsAutopilotSyncStatus(str, Enum):
    # Unknown sync status
    Unknown = "unknown",
    # Sync is in progress
    InProgress = "inProgress",
    # Sync completed.
    Completed = "completed",
    # Sync failed.
    Failed = "failed",

