from enum import Enum

class CopilotSearchResourceType(str, Enum):
    Unknown = "unknown",
    Site = "site",
    List_ = "list",
    ListItem = "listItem",
    Drive = "drive",
    DriveItem = "driveItem",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

