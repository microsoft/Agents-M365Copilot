from enum import Enum

class RecommendationFeatureAreas(str, Enum):
    Users = "users",
    Groups = "groups",
    Devices = "devices",
    Applications = "applications",
    AccessReviews = "accessReviews",
    ConditionalAccess = "conditionalAccess",
    Governance = "governance",
    UnknownFutureValue = "unknownFutureValue",

