from enum import Enum

class IncidentTaskSource(str, Enum):
    DefenderExpertsGuidedResponse = "defenderExpertsGuidedResponse",
    DefenderExpertsManagedResponse = "defenderExpertsManagedResponse",
    UnknownFutureValue = "unknownFutureValue",

