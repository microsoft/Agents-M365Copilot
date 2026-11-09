from enum import Enum

class NonEapAuthenticationMethodForEapTtlsType(str, Enum):
    # Unencrypted password (PAP).
    UnencryptedPassword = "unencryptedPassword",
    # Challenge Handshake Authentication Protocol (CHAP).
    ChallengeHandshakeAuthenticationProtocol = "challengeHandshakeAuthenticationProtocol",
    #  Microsoft CHAP (MS-CHAP).
    MicrosoftChap = "microsoftChap",
    # Microsoft CHAP Version 2 (MS-CHAP v2).
    MicrosoftChapVersionTwo = "microsoftChapVersionTwo",

