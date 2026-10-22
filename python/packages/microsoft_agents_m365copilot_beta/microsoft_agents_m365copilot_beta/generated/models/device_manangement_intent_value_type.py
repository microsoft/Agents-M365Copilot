from enum import Enum

class DeviceManangementIntentValueType(str, Enum):
    # The setting value is an integer
    Integer = "integer",
    # The setting value is a boolean
    Boolean = "boolean",
    # The setting value is a string
    String = "string",
    # The setting value is a complex object
    Complex = "complex",
    # The setting value is a collection
    Collection = "collection",
    # The setting value is an abstract complex object
    AbstractComplex = "abstractComplex",

