from enum import Enum

class AndroidPermissionActionType(str, Enum):
    Prompt = "prompt",
    AutoGrant = "autoGrant",
    AutoDeny = "autoDeny",

