from enum import Enum

class StudentAgeGroup(str, Enum):
    Minor = "minor",
    NotAdult = "notAdult",
    Adult = "adult",
    UnknownFutureValue = "unknownFutureValue",

