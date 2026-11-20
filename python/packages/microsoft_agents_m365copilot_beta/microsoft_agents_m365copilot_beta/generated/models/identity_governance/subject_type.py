from enum import Enum

class SubjectType(str, Enum):
    User = "user",
    AgentIdentity = "agentIdentity",
    UnknownFutureValue = "unknownFutureValue",
    ProvisioningObject = "provisioningObject",

