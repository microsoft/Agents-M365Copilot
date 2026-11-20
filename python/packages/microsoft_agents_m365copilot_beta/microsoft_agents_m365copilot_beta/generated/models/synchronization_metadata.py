from enum import Enum

class SynchronizationMetadata(str, Enum):
    GalleryApplicationIdentifier = "galleryApplicationIdentifier",
    GalleryApplicationKey = "galleryApplicationKey",
    IsOAuthEnabled = "isOAuthEnabled",
    IsSynchronizationAgentAssignmentRequired = "IsSynchronizationAgentAssignmentRequired",
    IsSynchronizationAgentRequired = "isSynchronizationAgentRequired",
    IsSynchronizationInPreview = "isSynchronizationInPreview",
    OAuthSettings = "oAuthSettings",
    SynchronizationLearnMoreIbizaFwLink = "synchronizationLearnMoreIbizaFwLink",
    ConfigurationFields = "configurationFields",

