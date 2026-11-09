from enum import Enum

class OpenIdConnectResponseMode(str, Enum):
    Form_post = "form_post",
    Query = "query",
    UnknownFutureValue = "unknownFutureValue",

