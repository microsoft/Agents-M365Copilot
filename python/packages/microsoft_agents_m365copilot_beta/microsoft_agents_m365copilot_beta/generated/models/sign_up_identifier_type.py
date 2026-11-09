from enum import Enum

class SignUpIdentifierType(str, Enum):
    EmailAddress = "emailAddress",
    UnknownFutureValue = "unknownFutureValue",
    Federation = "federation",

