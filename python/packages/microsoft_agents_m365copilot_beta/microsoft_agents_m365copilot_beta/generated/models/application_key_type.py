from enum import Enum

class ApplicationKeyType(str, Enum):
    ClientSecret = "clientSecret",
    Certificate = "certificate",
    UnknownFutureValue = "unknownFutureValue",

