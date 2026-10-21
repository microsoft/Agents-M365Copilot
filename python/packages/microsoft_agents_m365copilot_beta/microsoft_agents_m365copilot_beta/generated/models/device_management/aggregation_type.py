from enum import Enum

class AggregationType(str, Enum):
    Count = "count",
    Percentage = "percentage",
    AffectedCloudPcCount = "affectedCloudPcCount",
    AffectedCloudPcPercentage = "affectedCloudPcPercentage",
    UnknownFutureValue = "unknownFutureValue",
    DurationInMinutes = "durationInMinutes",

