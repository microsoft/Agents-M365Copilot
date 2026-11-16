from enum import Enum

class CloudPcUserSettingsPersistenceStorageSizeCategory(str, Enum):
    FourGB = "fourGB",
    EightGB = "eightGB",
    SixteenGB = "sixteenGB",
    ThirtyTwoGB = "thirtyTwoGB",
    SixtyFourGB = "sixtyFourGB",
    UnknownFutureValue = "unknownFutureValue",

