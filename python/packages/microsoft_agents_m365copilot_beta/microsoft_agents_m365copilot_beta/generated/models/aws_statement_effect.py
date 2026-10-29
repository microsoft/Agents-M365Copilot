from enum import Enum

class AwsStatementEffect(str, Enum):
    Allow = "allow",
    Deny = "deny",
    UnknownFutureValue = "unknownFutureValue",

