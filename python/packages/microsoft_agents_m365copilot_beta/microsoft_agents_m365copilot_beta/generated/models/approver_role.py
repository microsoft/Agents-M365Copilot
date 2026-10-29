from enum import Enum

class ApproverRole(str, Enum):
    Owner = "owner",
    Approver = "approver",
    UnknownFutureValue = "unknownFutureValue",

