from enum import Enum

class AuditAction(str, Enum):
    Link = "link",
    Unlink = "unlink",
    Update = "update",
    Delete = "delete",
    Create = "create",
    Upload = "upload",
    Download = "download",
    FileUploadMalwareDetected = "fileUploadMalwareDetected",
    UnknownFutureValue = "unknownFutureValue",

