from enum import Enum


class MessageUserRole(str, Enum):
    EnvelopeFrom = "envelopeFrom",
    HeaderFrom = "headerFrom",
    To = "to",
    Cc = "cc",
    Bcc = "bcc",
    UnknownFutureValue = "unknownFutureValue",

