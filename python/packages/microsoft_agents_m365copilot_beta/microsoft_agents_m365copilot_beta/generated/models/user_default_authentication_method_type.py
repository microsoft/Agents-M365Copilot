from enum import Enum

class UserDefaultAuthenticationMethodType(str, Enum):
    Push = "push",
    Oath = "oath",
    VoiceMobile = "voiceMobile",
    VoiceAlternateMobile = "voiceAlternateMobile",
    VoiceOffice = "voiceOffice",
    Sms = "sms",
    UnknownFutureValue = "unknownFutureValue",

