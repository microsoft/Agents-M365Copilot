from enum import Enum

class TeamsAppInstallationScopes(str, Enum):
    Team = "team",
    GroupChat = "groupChat",
    Personal = "personal",
    UnknownFutureValue = "unknownFutureValue",

