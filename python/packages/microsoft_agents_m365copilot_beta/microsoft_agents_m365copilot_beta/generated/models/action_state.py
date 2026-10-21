from enum import Enum

class ActionState(str, Enum):
    None_ = "none",
    Pending = "pending",
    Canceled = "canceled",
    Active = "active",
    Done = "done",
    Failed = "failed",
    NotSupported = "notSupported",

