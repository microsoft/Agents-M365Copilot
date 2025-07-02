from enum import Enum

class RetrievalDataSource(str, Enum):
    SharePoint = "sharePoint",
    OneDriveBusiness = "oneDriveBusiness",
    ExternalItems = "externalItems",
    Mail = "mail",
    Calendar = "calendar",
    Teams = "teams",
    People = "people",
    SharePointEmbedded = "sharePointEmbedded",
    UnknownFutureValue = "unknownFutureValue",

