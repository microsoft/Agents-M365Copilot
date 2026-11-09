from enum import Enum

class MfaType(str, Enum):
    Eotp = "eotp",
    OneWaySms = "oneWaySms",
    TwoWaySms = "twoWaySms",
    TwoWaySmsOtherMobile = "twoWaySmsOtherMobile",
    PhoneAppNotification = "phoneAppNotification",
    PhoneAppOtp = "phoneAppOtp",
    TwoWayVoiceMobile = "twoWayVoiceMobile",
    TwoWayVoiceOffice = "twoWayVoiceOffice",
    TwoWayVoiceOtherMobile = "twoWayVoiceOtherMobile",
    Fido = "fido",
    Certificate = "certificate",
    Other = "other",
    UnknownFutureValue = "unknownFutureValue",

