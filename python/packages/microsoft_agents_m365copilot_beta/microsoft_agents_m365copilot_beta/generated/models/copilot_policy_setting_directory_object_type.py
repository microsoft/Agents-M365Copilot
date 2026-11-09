from enum import Enum

class CopilotPolicySettingDirectoryObjectType(str, Enum):
    # A user.
    User = "user",
    # A group.
    Group = "group",
    # An agent application identifier.
    AgentAppId = "agentAppId",
    # An agent user.
    AgentUser = "agentUser",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

