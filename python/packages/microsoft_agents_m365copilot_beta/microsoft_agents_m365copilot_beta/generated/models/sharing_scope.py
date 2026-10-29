from enum import Enum

class SharingScope(str, Enum):
    Anyone = "anyone",
    Organization = "organization",
    SpecificPeople = "specificPeople",
    Anonymous = "anonymous",
    Users = "users",
    UnknownFutureValue = "unknownFutureValue",

