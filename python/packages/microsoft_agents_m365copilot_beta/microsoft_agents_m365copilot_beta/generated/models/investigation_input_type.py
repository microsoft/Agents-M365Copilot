from enum import Enum

class InvestigationInputType(str, Enum):
    DefenderIncidentId = "defenderIncidentId",
    DefenderAlertId = "defenderAlertId",
    DefenderThreatIntelligenceId = "defenderThreatIntelligenceId",
    AzureSubscriptionId = "azureSubscriptionId",
    AzureIdentityId = "azureIdentityId",
    Keyword = "keyword",
    UnknownFutureValue = "unknownFutureValue",

