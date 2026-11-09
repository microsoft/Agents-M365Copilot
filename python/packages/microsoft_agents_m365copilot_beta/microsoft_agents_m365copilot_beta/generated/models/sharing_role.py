from enum import Enum

class SharingRole(str, Enum):
    None_ = "none",
    View = "view",
    Edit = "edit",
    ManageList = "manageList",
    Review = "review",
    RestrictedView = "restrictedView",
    SubmitOnly = "submitOnly",
    UnknownFutureValue = "unknownFutureValue",

