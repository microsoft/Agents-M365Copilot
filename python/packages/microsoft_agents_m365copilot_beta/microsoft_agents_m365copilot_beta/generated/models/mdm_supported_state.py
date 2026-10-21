from enum import Enum

class MdmSupportedState(str, Enum):
    # Mdm support status of the setting is not known.
    Unknown = "unknown",
    # Setting is supported.
    Supported = "supported",
    # Setting is unsupported.
    Unsupported = "unsupported",
    # Setting is depcrecated.
    Deprecated = "deprecated",

