from enum import Enum

class ManagementParameterValueType(str, Enum):
    String = "string",
    Integer = "integer",
    Boolean = "boolean",
    Guid = "guid",
    StringCollection = "stringCollection",
    IntegerCollection = "integerCollection",
    BooleanCollection = "booleanCollection",
    GuidCollection = "guidCollection",
    UnknownFutureValue = "unknownFutureValue",

