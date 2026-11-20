from enum import Enum

class ServiceStartType(str, Enum):
    # Manual service start type(default)
    Manual = "manual",
    # Automatic service start type
    Automatic = "automatic",
    # Service start type disabled
    Disabled = "disabled",

