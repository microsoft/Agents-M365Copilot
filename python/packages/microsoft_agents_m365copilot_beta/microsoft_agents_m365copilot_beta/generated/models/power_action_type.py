from enum import Enum

class PowerActionType(str, Enum):
    # Not configured
    NotConfigured = "notConfigured",
    # No action
    NoAction = "noAction",
    # Put device in sleep state
    Sleep = "sleep",
    # Put device in hibernate state
    Hibernate = "hibernate",
    # Shutdown device
    Shutdown = "shutdown",

