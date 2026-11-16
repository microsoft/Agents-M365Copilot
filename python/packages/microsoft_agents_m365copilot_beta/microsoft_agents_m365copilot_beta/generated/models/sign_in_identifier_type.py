from enum import Enum

class SignInIdentifierType(str, Enum):
    UserPrincipalName = "userPrincipalName",
    PhoneNumber = "phoneNumber",
    ProxyAddress = "proxyAddress",
    QrCode = "qrCode",
    OnPremisesUserPrincipalName = "onPremisesUserPrincipalName",
    UnknownFutureValue = "unknownFutureValue",

