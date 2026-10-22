from enum import Enum

class OpenIdConnectResponseTypes(str, Enum):
    Code = "code",
    Id_token = "id_token",
    Token = "token",

