from enum import Enum

class RedundancyTier(str, Enum):
    NoRedundancy = "noRedundancy",
    ZoneRedundancy = "zoneRedundancy",
    UnknownFutureValue = "unknownFutureValue",

