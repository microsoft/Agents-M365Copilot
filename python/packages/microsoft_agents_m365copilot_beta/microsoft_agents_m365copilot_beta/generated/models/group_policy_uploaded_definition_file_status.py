from enum import Enum

class GroupPolicyUploadedDefinitionFileStatus(str, Enum):
    # Group Policy uploaded definition file invalid upload status.
    None_ = "none",
    # Group Policy uploaded definition file upload in progress.
    UploadInProgress = "uploadInProgress",
    # Group Policy uploaded definition file available.
    Available = "available",
    # Group Policy uploaded definition file assigned to policy.
    Assigned = "assigned",
    # Group Policy uploaded definition file removal in progress.
    RemovalInProgress = "removalInProgress",
    # Group Policy uploaded definition file upload failed.
    UploadFailed = "uploadFailed",
    # Group Policy uploaded definition file removal failed.
    RemovalFailed = "removalFailed",

