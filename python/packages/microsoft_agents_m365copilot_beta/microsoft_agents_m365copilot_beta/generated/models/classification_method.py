from enum import Enum

class ClassificationMethod(str, Enum):
    PatternMatch = "patternMatch",
    ExactDataMatch = "exactDataMatch",
    Fingerprint = "fingerprint",
    MachineLearning = "machineLearning",
    PrivacyDataMatch = "privacyDataMatch",
    AiPowered = "aiPowered",
    UnknownFutureValue = "unknownFutureValue",

