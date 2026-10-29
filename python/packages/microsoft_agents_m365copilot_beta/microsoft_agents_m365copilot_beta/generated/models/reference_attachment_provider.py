from enum import Enum

class ReferenceAttachmentProvider(str, Enum):
    Other = "other",
    OneDriveBusiness = "oneDriveBusiness",
    OneDriveConsumer = "oneDriveConsumer",
    Dropbox = "dropbox",

