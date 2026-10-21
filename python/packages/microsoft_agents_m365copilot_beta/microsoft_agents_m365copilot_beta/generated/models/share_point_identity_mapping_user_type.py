from enum import Enum

class SharePointIdentityMappingUserType(str, Enum):
    None_ = "none",
    RegularUser = "regularUser",
    AdminUser = "adminUser",
    GuestUser = "guestUser",
    UnknownFutureValue = "unknownFutureValue",

