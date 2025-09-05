from enum import Enum

class RetrievalDataSource(str, Enum):
    SharePoint = "sharePoint",
    OneDriveBusiness = "oneDriveBusiness",
    ExternalItem = "externalItem",
    UnknownFutureValue = "unknownFutureValue",

