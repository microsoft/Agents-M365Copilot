from enum import Enum

class AuthenticationAppAdminConfiguration(str, Enum):
    NotApplicable = "notApplicable",
    Enabled = "enabled",
    Disabled = "disabled",
    UnknownFutureValue = "unknownFutureValue",

