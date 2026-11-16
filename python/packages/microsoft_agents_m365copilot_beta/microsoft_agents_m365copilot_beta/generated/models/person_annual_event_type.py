from enum import Enum

class PersonAnnualEventType(str, Enum):
    Birthday = "birthday",
    Wedding = "wedding",
    Work = "work",
    Other = "other",
    UnknownFutureValue = "unknownFutureValue",

