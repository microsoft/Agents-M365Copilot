from enum import Enum

class RecommendationStatus(str, Enum):
    Active = "active",
    CompletedBySystem = "completedBySystem",
    CompletedByUser = "completedByUser",
    Dismissed = "dismissed",
    Postponed = "postponed",
    UnknownFutureValue = "unknownFutureValue",
    RiskAccepted = "riskAccepted",
    ThirdParty = "thirdParty",
    Planned = "planned",
    AlternateMitigation = "alternateMitigation",
    NeedsMoreAction = "needsMoreAction",

