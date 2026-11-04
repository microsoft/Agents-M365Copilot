from enum import Enum

class RecommendationCategoryGroup(str, Enum):
    StrengthenAuthentication = "strengthenAuthentication",
    DetectAndRespondToThreats = "detectAndRespondToThreats",
    EnforceLeastPrivilege = "enforceLeastPrivilege",
    GovernAppsCredentialsAndAgents = "governAppsCredentialsAndAgents",
    HardenInfrastructure = "hardenInfrastructure",
    DefenderForIdentity = "defenderForIdentity",
    UnknownFutureValue = "unknownFutureValue",

