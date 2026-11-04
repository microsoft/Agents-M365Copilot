from enum import Enum

class AppInfoDataRetentionPolicy(str, Enum):
    DataRetained = "dataRetained",
    DeletedImmediately = "deletedImmediately",
    DeletedWithinTwoWeeks = "deletedWithinTwoWeeks",
    DeletedWithinOneMonth = "deletedWithinOneMonth",
    DeletedWithinThreeMonths = "deletedWithinThreeMonths",
    DeletedWithinMoreThanThreeMonths = "deletedWithinMoreThanThreeMonths",
    Unknown = "unknown",
    UnknownFutureValue = "unknownFutureValue",

