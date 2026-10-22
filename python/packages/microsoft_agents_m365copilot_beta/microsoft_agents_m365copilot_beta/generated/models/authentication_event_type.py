from enum import Enum

class AuthenticationEventType(str, Enum):
    TokenIssuanceStart = "tokenIssuanceStart",
    PageRenderStart = "pageRenderStart",
    UnknownFutureValue = "unknownFutureValue",
    AttributeCollectionStart = "attributeCollectionStart",
    AttributeCollectionSubmit = "attributeCollectionSubmit",
    EmailOtpSend = "emailOtpSend",
    PasswordSubmit = "passwordSubmit",

