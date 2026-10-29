from enum import Enum

class DefaultMfaMethodType(str, Enum):
    None_ = "none",
    MobilePhone = "mobilePhone",
    AlternateMobilePhone = "alternateMobilePhone",
    OfficePhone = "officePhone",
    MicrosoftAuthenticatorPush = "microsoftAuthenticatorPush",
    SoftwareOneTimePasscode = "softwareOneTimePasscode",
    UnknownFutureValue = "unknownFutureValue",

