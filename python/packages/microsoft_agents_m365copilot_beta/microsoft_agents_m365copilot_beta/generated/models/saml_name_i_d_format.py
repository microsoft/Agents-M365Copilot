from enum import Enum

class SamlNameIDFormat(str, Enum):
    Default = "default",
    Unspecified = "unspecified",
    EmailAddress = "emailAddress",
    WindowsDomainQualifiedName = "windowsDomainQualifiedName",
    Persistent = "persistent",
    UnknownFutureValue = "unknownFutureValue",

