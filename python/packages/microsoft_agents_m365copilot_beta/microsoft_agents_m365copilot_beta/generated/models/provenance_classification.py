from enum import Enum

class ProvenanceClassification(str, Enum):
    HighAssurance = "highAssurance",
    MediumAssurance = "mediumAssurance",
    LowAssurance = "lowAssurance",
    UnknownFutureValue = "unknownFutureValue",

