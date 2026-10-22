from enum import Enum

class AwsSecurityToolWebServices(str, Enum):
    Macie = "macie",
    WafShield = "wafShield",
    CloudTrail = "cloudTrail",
    Inspector = "inspector",
    SecurityHub = "securityHub",
    Detective = "detective",
    GuardDuty = "guardDuty",
    UnknownFutureValue = "unknownFutureValue",

