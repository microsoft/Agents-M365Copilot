from enum import Enum

class RepositoryType(str, Enum):
    # GitHub.
    GitHub = "gitHub",
    # Azure DevOps.
    AzureDevOps = "azureDevOps",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

