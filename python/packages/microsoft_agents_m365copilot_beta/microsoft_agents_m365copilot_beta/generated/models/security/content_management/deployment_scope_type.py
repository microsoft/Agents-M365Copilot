from enum import Enum

class DeploymentScopeType(str, Enum):
    # Azure resource group.
    ResourceGroup = "resourceGroup",
    # Azure management group.
    ManagementGroup = "managementGroup",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

