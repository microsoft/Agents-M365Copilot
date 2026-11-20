from enum import Enum

class MobileThreatDefensePartnerPriority(str, Enum):
    # Indicates use of Microsoft Defender Endpoint over 3rd party MTD connectors
    DefenderOverThirdPartyPartner = "defenderOverThirdPartyPartner",
    # Indicates use of a 3rd party MTD connector over Microsoft Defender Endpoint
    ThirdPartyPartnerOverDefender = "thirdPartyPartnerOverDefender",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

