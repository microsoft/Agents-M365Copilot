from enum import Enum

class WindowsAutopilotProfileAssignmentStatus(str, Enum):
    # Unknown assignment status
    Unknown = "unknown",
    # Assigned successfully in Intune and in sync with Windows auto pilot program
    AssignedInSync = "assignedInSync",
    # Assigned successfully in Intune and not in sync with Windows auto pilot program
    AssignedOutOfSync = "assignedOutOfSync",
    # Assigned successfully in Intune and either in-sync or out of sync with Windows auto pilot program
    AssignedUnkownSyncState = "assignedUnkownSyncState",
    # Not assigned
    NotAssigned = "notAssigned",
    # Pending assignment
    Pending = "pending",
    #  Assignment failed
    Failed = "failed",

