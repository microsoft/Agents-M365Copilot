from enum import Enum

class SensitiveTypeScope(str, Enum):
    FullDocument = "fullDocument",
    PartialDocument = "partialDocument",

