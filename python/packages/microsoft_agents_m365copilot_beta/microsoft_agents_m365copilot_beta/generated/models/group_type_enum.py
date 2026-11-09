from enum import Enum

class GroupTypeEnum(str, Enum):
    IsCloudGroup = "isCloudGroup",
    IsOnPremiseGroup = "isOnPremiseGroup",
    IsSoftDeletedGroup = "isSoftDeletedGroup",

