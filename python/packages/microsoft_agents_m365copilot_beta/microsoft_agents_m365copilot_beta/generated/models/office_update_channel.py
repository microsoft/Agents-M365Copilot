from enum import Enum

class OfficeUpdateChannel(str, Enum):
    None_ = "none",
    Current = "current",
    Deferred = "deferred",
    FirstReleaseCurrent = "firstReleaseCurrent",
    FirstReleaseDeferred = "firstReleaseDeferred",
    MonthlyEnterprise = "monthlyEnterprise",

