from enum import Enum

class TeamworkSupportedClient(str, Enum):
    Unknown = "unknown",
    SkypeDefaultAndTeams = "skypeDefaultAndTeams",
    TeamsDefaultAndSkype = "teamsDefaultAndSkype",
    SkypeOnly = "skypeOnly",
    TeamsOnly = "teamsOnly",
    UnknownFutureValue = "unknownFutureValue",

