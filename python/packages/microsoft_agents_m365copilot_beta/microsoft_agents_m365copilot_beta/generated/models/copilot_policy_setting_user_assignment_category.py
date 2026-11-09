from enum import Enum

class CopilotPolicySettingUserAssignmentCategory(str, Enum):
    # All users are assigned.
    Everyone = "everyone",
    # No users are assigned.
    NoOne = "noOne",
    # Only explicitly selected users are assigned.
    SpecificUsers = "specificUsers",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

