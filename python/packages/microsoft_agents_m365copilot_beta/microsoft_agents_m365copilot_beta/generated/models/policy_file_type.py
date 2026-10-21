from enum import Enum

class PolicyFileType(str, Enum):
    DlpPolicy = "dlpPolicy",
    DlpSensitiveInformationType = "dlpSensitiveInformationType",
    DataCollectionPolicy = "dataCollectionPolicy",
    UnknownFutureValue = "unknownFutureValue",

