from enum import Enum

class DeviceCustomAttributeValueType(str, Enum):
    # Indicates the value for a custom attribute script is an integer.
    Integer = "integer",
    # Indicates the value for a custom attribute script is a string.
    String = "string",
    # Indicates the value for a custom attribute script is a date conforming to ISO 8601.
    DateTime = "dateTime",

