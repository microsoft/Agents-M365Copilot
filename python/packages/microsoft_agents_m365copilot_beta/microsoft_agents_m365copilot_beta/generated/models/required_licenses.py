from enum import Enum

class RequiredLicenses(str, Enum):
    NotApplicable = "notApplicable",
    MicrosoftEntraIdFree = "microsoftEntraIdFree",
    MicrosoftEntraIdP1 = "microsoftEntraIdP1",
    MicrosoftEntraIdP2 = "microsoftEntraIdP2",
    MicrosoftEntraIdGovernance = "microsoftEntraIdGovernance",
    MicrosoftEntraWorkloadId = "microsoftEntraWorkloadId",
    UnknownFutureValue = "unknownFutureValue",
    Aatp = "aatp",
    MicrosoftEntraSuite = "microsoftEntraSuite",

