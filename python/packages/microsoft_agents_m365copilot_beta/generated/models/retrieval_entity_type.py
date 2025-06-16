from enum import Enum


class RetrievalEntityType(str, Enum):
    Site = "site",
    List_ = "list",
    ListItem = "listItem",
    Drive = "drive",
    DriveItem = "driveItem",
    ExternalItem = "externalItem",
    UnknownFutureValue = "unknownFutureValue",

