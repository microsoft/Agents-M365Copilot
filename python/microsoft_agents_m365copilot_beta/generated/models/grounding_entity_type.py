from enum import Enum

class GroundingEntityType(str, Enum):
    Site = "site",
    List_ = "list",
    ListItem = "listItem",
    Drive = "drive",
    DriveItem = "driveItem",
    UnknownFutureValue = "unknownFutureValue",

