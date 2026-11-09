from enum import Enum

class SharePointIdentityMappingGroupType(str, Enum):
    None_ = "none",
    RegularGroup = "regularGroup",
    M365Group = "m365Group",
    UnknownFutureValue = "unknownFutureValue",

