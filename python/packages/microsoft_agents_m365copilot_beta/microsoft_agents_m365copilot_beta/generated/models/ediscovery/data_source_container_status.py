from enum import Enum

class DataSourceContainerStatus(str, Enum):
    Active = "Active",
    Released = "Released",
    UnknownFutureValue = "UnknownFutureValue",

