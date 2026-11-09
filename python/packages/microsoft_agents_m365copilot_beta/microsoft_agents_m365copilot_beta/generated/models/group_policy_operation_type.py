from enum import Enum

class GroupPolicyOperationType(str, Enum):
    # Group Policy invalid operation type.
    None_ = "none",
    # Group Policy upload operation type.
    Upload = "upload",
    # Group Policy upload new version operation type.
    UploadNewVersion = "uploadNewVersion",
    # Group Policy add new language(ADML) files operation type.
    AddLanguageFiles = "addLanguageFiles",
    # Group Policy remove language(ADML) files operation type.
    RemoveLanguageFiles = "removeLanguageFiles",
    # Group Policy update language(ADML) files operation type.
    UpdateLanguageFiles = "updateLanguageFiles",
    # Group Policy remove uploaded file operation type.
    Remove = "remove",

