from enum import Enum

class EncryptWith(str, Enum):
    Template = "template",
    UserDefinedRights = "userDefinedRights",

