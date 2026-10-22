from enum import Enum

class EntityDefinitionInputRole(str, Enum):
    Impacted = "impacted",
    Related = "related",
    UnknownFutureValue = "unknownFutureValue",

