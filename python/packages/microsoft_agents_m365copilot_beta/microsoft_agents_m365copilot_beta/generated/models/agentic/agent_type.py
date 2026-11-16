from enum import Enum

class AgentType(str, Enum):
    NotAgentic = "notAgentic",
    AgenticApp = "agenticApp",
    AgenticAppInstance = "agenticAppInstance",
    AgentIdentityBlueprintPrincipal = "agentIdentityBlueprintPrincipal",
    AgentIDuser = "agentIDuser",
    UnknownFutureValue = "unknownFutureValue",

