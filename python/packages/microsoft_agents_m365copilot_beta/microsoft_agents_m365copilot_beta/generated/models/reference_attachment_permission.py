from enum import Enum

class ReferenceAttachmentPermission(str, Enum):
    Other = "other",
    View = "view",
    Edit = "edit",
    AnonymousView = "anonymousView",
    AnonymousEdit = "anonymousEdit",
    OrganizationView = "organizationView",
    OrganizationEdit = "organizationEdit",

