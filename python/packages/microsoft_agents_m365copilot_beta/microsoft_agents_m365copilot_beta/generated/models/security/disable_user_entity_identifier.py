from enum import Enum

class DisableUserEntityIdentifier(str, Enum):
    AccountSid = "accountSid",
    InitiatingProcessAccountSid = "initiatingProcessAccountSid",
    RequestAccountSid = "requestAccountSid",
    OnPremSid = "onPremSid",
    UnknownFutureValue = "unknownFutureValue",

