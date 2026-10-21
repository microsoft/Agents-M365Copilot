from enum import Enum

class ResourceQuotaType(str, Enum):
    AgentIdentityBlueprint = "agentIdentityBlueprint",
    AgentIdentity = "agentIdentity",
    ManagedIdentity = "managedIdentity",
    UnknownFutureValue = "unknownFutureValue",

