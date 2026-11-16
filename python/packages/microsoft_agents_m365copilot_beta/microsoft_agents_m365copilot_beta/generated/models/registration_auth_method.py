from enum import Enum

class RegistrationAuthMethod(str, Enum):
    Email = "email",
    MobilePhone = "mobilePhone",
    OfficePhone = "officePhone",
    SecurityQuestion = "securityQuestion",
    AppNotification = "appNotification",
    AppCode = "appCode",
    AlternateMobilePhone = "alternateMobilePhone",
    Fido = "fido",
    AppPassword = "appPassword",
    UnknownFutureValue = "unknownFutureValue",
    ExternalAuthMethod = "externalAuthMethod",

