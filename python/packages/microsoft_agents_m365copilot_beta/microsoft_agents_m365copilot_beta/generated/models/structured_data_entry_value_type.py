from enum import Enum

class StructuredDataEntryValueType(str, Enum):
    DateTime = "dateTime",
    Boolean = "boolean",
    Byte = "byte",
    String = "string",
    Integer32 = "integer32",
    UnsignedInteger32 = "unsignedInteger32",
    Integer64 = "integer64",
    UnsignedInteger64 = "unsignedInteger64",
    StringArray = "stringArray",
    ByteArray = "byteArray",
    UnknownFutureValue = "unknownFutureValue",

