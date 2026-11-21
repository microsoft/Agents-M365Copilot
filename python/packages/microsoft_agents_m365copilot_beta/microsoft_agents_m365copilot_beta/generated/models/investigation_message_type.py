from enum import Enum

class InvestigationMessageType(str, Enum):
    UserMessage = "userMessage",
    AgentMessage = "agentMessage",
    ToolRequest = "toolRequest",
    ToolOutput = "toolOutput",
    PermissionRequest = "permissionRequest",
    PermissionResponse = "permissionResponse",
    UnknownFutureValue = "unknownFutureValue",

