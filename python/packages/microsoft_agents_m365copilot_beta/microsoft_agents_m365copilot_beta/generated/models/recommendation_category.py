from enum import Enum

class RecommendationCategory(str, Enum):
    IdentityBestPractice = "identityBestPractice",
    IdentitySecureScore = "identitySecureScore",
    UnknownFutureValue = "unknownFutureValue",
    MdiSecureScore = "mdiSecureScore",

