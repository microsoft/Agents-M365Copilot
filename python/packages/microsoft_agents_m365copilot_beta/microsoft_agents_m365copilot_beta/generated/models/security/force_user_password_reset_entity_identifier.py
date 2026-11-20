from enum import Enum

class ForceUserPasswordResetEntityIdentifier(str, Enum):
    AccountSid = "accountSid",
    InitiatingProcessAccountSid = "initiatingProcessAccountSid",
    RequestAccountSid = "requestAccountSid",
    OnPremSid = "onPremSid",
    UnknownFutureValue = "unknownFutureValue",

