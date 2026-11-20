from enum import Enum

class NonEapAuthenticationMethodForPeap(str, Enum):
    # None.
    None_ = "none",
    # Microsoft CHAP Version 2 (MS-CHAP v2).
    MicrosoftChapVersionTwo = "microsoftChapVersionTwo",

