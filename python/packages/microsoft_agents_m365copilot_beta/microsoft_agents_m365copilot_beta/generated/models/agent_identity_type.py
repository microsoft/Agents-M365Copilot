from enum import Enum

class AgentIdentityType(str, Enum):
    AgentIdentity = "agentIdentity",
    AgentUser = "agentUser",
    UnknownFutureValue = "unknownFutureValue",
    AgentIdentityBlueprintPrincipal = "agentIdentityBlueprintPrincipal",
    User = "user",
    DiscoveredAgentIdentity = "discoveredAgentIdentity",

