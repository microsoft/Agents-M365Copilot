from enum import Enum

class AndroidManagedStoreAppConfigurationSchemaItemDataType(str, Enum):
    Bool = "bool",
    Integer = "integer",
    String = "string",
    Choice = "choice",
    Multiselect = "multiselect",
    Bundle = "bundle",
    BundleArray = "bundleArray",
    Hidden = "hidden",

