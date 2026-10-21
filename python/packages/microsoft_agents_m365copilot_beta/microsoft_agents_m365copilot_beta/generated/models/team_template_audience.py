from enum import Enum

class TeamTemplateAudience(str, Enum):
    Organization = "organization",
    User = "user",
    Public = "public",
    UnknownFutureValue = "unknownFutureValue",

