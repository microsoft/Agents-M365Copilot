from enum import Enum

class CampaignStatus(str, Enum):
    Unknown = "unknown",
    Draft = "draft",
    InProgress = "inProgress",
    Scheduled = "scheduled",
    Completed = "completed",
    Failed = "failed",
    Cancelled = "cancelled",
    Excluded = "excluded",
    Deleted = "deleted",
    UnknownFutureValue = "unknownFutureValue",

